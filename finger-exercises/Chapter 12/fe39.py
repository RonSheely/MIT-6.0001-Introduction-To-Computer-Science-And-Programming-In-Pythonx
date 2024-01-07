"""Finger exercise: Use merge_sort to sort a list to tuples of integers.
The sorting order should be determined by the sum of the integers in
the tuple. For example, (5, 2) should precede (1, 8) and follow (1,
2, 3)."""


def merge(left, right, compare):
    """Assumes left and right are sorted lists and compare defines
       an ordering on the elements.
       Returns a new sorted (by compare) list cotaining the same
       elements as (left + right) would contain"""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(sum(left[i]), sum(right[j])):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(L, compare=lambda x, y: x < y):
    """Assumes L is a list, compare defines an ordering
        on elements of L
        Returns a new sorted list with the same elements as L"""
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


list_of_tuples_with_ints = [(5, 2), (1, 8), (3, 4), (1, 1)]
print(merge_sort(list_of_tuples_with_ints))
