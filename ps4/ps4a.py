def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) == 1:
        return sequence
    permutations = []
    for i in range(len(sequence)):
        firstChar = sequence[i]
        remainingChars = sequence[:i] + sequence[i+1:]
        for perm in get_permutations(remainingChars):
            if firstChar + perm not in permutations:
                permutations.append(firstChar + perm)
    return permutations

if __name__ == '__main__':
#    #EXAMPLE
    
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    

#    print(len(get_permutations('aaabcd')))