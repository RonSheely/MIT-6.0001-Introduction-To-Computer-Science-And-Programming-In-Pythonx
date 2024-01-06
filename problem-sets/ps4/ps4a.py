# Problem Set 4A
# Name: <Ezra Weaver>
# Collaborators:
# Time Spent: x:xx

def add_char(string, char):
    empty_list = [char + string]
    for x in range(len(string)):
        new_string = string[x:] + char + string[:x]
        empty_list.append(new_string)
    return empty_list


def get_permutations(sequence):
    """
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """
    if len(sequence) == 1:
        return [sequence]
    char = sequence[0]
    sample = get_permutations(sequence[1:])
    final_list = []
    for x in sample:
        final_list = final_list + add_char(x, char)
    return final_list


if __name__ == '__main__':
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'bca', 'cab', 'acb', 'cba', 'bac'])
    print('Actual Output:', get_permutations(example_input))


