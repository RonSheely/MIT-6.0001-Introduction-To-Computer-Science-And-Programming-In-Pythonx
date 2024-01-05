"""Finger exercise: Add a method satisfying the specification below
to the Int_set class."""


class IntSet(object):
    """An IntSet is a set of integers"""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except ValueError:
            raise ValueError(str(e) + ' not found')

    def get_members(self):
        """Returns a list containing the elements of self._
        Nothing can be assumed about the order of the elements"""
        return self.vals[:]

    def __add__(self, other):
        """other is an Int_set
        mutates self so that it contains exactly the
        elemnts in self
        plus the elements in others."""
        for num in other.vals[:]:
            if num not in self.vals:
                self.vals.append(num)

    def __str__(self):
        """Returns a string representation of self"""
        if not self.vals:
            return '{}'
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return f"{{{result[:-1]}}}"


x = Int_set()
y = Int_set()

x.insert(1)
x.insert(2)
y.insert(2)
y.insert(3)

x + y
print(x)
