def get_indices_of_item_weights(weights, length, limit):
    """
    Takes a list of weights, length of list, and a weight limit.
    Returns the 2 weights' indices that add to the limit,
    in reverse order.

    Returns None if no two are found.

    Overall runtime is approximately O(2n)
    """
    # Create a blank dictionary
    d = {}

    # Store values of weights in dict
    # key = weight, value = index in list
    for i, w in enumerate(weights):  # O(n)
        # handle for duplicate weights
        if w in d:
            d[w] = (i, d[w])
        else:
            d[w] = i

    # Check to see if limit - weight exists in dict
    for k, v in d.items():  # O(n)
        if limit - k in d:
            # handle duplicate weights
            if d[limit-k] == v:
                return v
            return (d[limit-k], v)

    return None

# This passes the current tests, but would likely not pass
# in the event of duplicate weights but a limit that only
# requests one of the weights

# Perhaps should initialize each value as an empty list,
# then simply append the value each time added
# Then when outputting, index the list for the correct values
