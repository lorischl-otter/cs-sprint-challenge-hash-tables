def has_negatives(a):
    """
    Takes a list `a`
    Returns all positive values from list which
    also had corresponding negative numbers in the list.

    Overall runtime around O(2n) or O(n) over length a
    """
    # Create empty dict
    d = {}

    # Add values of a to dict
    for x in a:  # O(n) over a
        d[x] = True

    # Create result as empty list
    result = []

    # Look for negative values in dict
    for x in a:  # O(n) over a
        # if x is positive, and -x in dict
        # add to results
        if x > 0 and -x in d:
            result.append(x)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
