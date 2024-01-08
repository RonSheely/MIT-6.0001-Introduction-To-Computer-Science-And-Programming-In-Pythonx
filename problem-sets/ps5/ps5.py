# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
import traceback
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


# -----------------------------------------------------------------------

# ======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
# ======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    if url == "https://news.yahoo.com/rss/topstories":
        return []
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
        #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
        #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret


# ======================
# Data structure design
# ======================

# Problem 1

class NewsStory(object):

    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError


class PhraseTrigger(Trigger):

    def __init__(self, phrase):
        assert not any(char in string.punctuation for char in phrase), "Phrase must not contain punctuation"
        self.phrase = phrase.lower()
        self.phrase_words = self.phrase.split()

    def is_phrase_in(self, text):
        text = text.lower()
        text_list = list(text)
        for i, char in enumerate(text):
            if char in string.punctuation:
                text_list[i] = " "
        text = "".join(text_list).split()
        for y, word in enumerate(text):
            if word in self.phrase_words:
                for i in range(len(self.phrase_words)):
                    if text[y + i] != self.phrase_words[i]:
                        return False
                return True
        return False
        # text = " ".join("".join(text_list).split())   # This is how I would implement this code
        # return self.phrase in text             # I prefer the output this gives over what's stated in the assignment


class TitleTrigger(PhraseTrigger):

    def __init__(self, phrase):
        super().__init__(phrase)

    def evaluate(self, story):
        title = story.get_title()
        return self.is_phrase_in(title)


class DescriptionTrigger(PhraseTrigger):

    def __init__(self, phrase):
        super().__init__(phrase)

    def evaluate(self, story):
        description = story.get_description()
        return self.is_phrase_in(description)


class TimeTrigger(Trigger):

    def __init__(self, input_time):
        """input_time must be in the format of %d %b %Y %H:%M:%S
           example: 3 Oct 2016 17:00:10"""
        self.datetime_obj = datetime.strptime(input_time.strip(), "%d %b %Y %H:%M:%S")


class BeforeTrigger(TimeTrigger):

    def __init__(self, input_time):
        super().__init__(input_time)

    def evaluate(self, story):
        return story.get_pubdate() < self.datetime_obj


class AfterTrigger(TimeTrigger):

    def __init__(self, input_time):
        super().__init__(input_time)

    def evaluate(self, story):
        return story.get_pubdate() > self.datetime_obj


class NotTrigger(Trigger):

    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)


class AndTrigger(Trigger):

    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)


class OrTrigger(Trigger):

    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)


# ======================
# Filtering
# ======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filtered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) is True:
                filtered_stories.append(story)
    return filtered_stories


TRIGGERS_CONSTANT = {"TITLE": TitleTrigger, "DESCRIPTION": DescriptionTrigger,
                     "AFTER": AfterTrigger, "BEFORE": BeforeTrigger, "NOT": NotTrigger,
                     "AND": AndTrigger, "OR": OrTrigger}


def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    known_triggers = {}
    added_triggers = []
    for command_entry in lines:
        command_entry = command_entry.split(",")
        if command_entry[1] in ["AND", "NOT", "OR"]:
            known_triggers[command_entry[0]] = TRIGGERS_CONSTANT[command_entry[1]](
                known_triggers[command_entry[2]], known_triggers[command_entry[3]])
        elif command_entry[0] == "ADD":
            for command in command_entry[1:]:
                added_triggers.append(known_triggers[command])
        else:
            known_triggers[command_entry[0]] = TRIGGERS_CONSTANT[command_entry[1]](command_entry[2])
    return added_triggers


SLEEPTIME = 120  # seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        triggerlist = read_trigger_config('triggers.txt')
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica", 14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []

        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title() + "\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:
            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("https://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("https://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)

            print("Sleeping...")
            time.sleep(SLEEPTIME)
    except AttributeError as e:
        print("\n", e)
        # traceback.print_exc()


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
