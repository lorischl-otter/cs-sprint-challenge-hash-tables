def intersection(arrays):
    """
    Takes a list of up to 10 arrays with up to 1 million values each.
    Returns the numbers that appear in all provided lists.
    """

    # Initialize dict with 10 blank dicts as values
    d = {l: {} for l in range(1, 11)}

    # Create dictionary from values in first list
    for i, n in enumerate(arrays[0]):  # O(n) over length of list 1
        d[1][n] = i

    # Compare subsequent lists to first dict keys
    # Only take overlapping values to add to next dict
    for i in range(1, len(arrays[1:])+1):  # O(n) over # of lists
        for j, n in enumerate(arrays[i]):  # O(n) over length of lists
            if n in d[i]:  # O(1)
                d[i+1][n] = i

    # The result is only the values which were in the final nested
    # dictionary, as they were the only values in all lists
    result = list(d[len(arrays)].keys())

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
