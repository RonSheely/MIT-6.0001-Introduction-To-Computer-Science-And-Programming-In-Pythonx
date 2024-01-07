"""Finger exercise: Why does the code use mid+1 rather than mid in
the second recursive call?"""


def search(L, e):
    """Assumes L is a list, the elements of
       which are in ascending order."""

    def bin_search(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bin_search(L, e, mid + 1, high)  # mid is mid + 1 to avoid overlapping search areas

    if len(L) == 0:
        return False
    else:
        return bin_search(L, e, 0, len(L) - 1)
