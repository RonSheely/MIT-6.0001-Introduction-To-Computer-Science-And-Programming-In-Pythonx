"""Finger exercise: Use find to implement a function satisfying the
specification"""


test_string = "bobisabuilder"
compare_string = "bis"


def find_last(s: str, sub: str) -> int:
    """s and sub are non-empty strings
    Returns the index of the last occurrence of sub in s.
    Returns None if sub does not occur in s"""
    sub_length = len(sub)
    if sub in s:
        found = []
        low = 0
        high = sub_length - 1
        for x in range(len(s)):
            if s[low:high + 1] == sub:
                found.append(low)
            low += 1
            high += 1
        return max(found)
    return None


verified_results = test_string.find(compare_string)
results = find_last(test_string, compare_string)

print(results == verified_results)
