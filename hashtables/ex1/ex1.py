def get_indices_of_item_weights(weights, length, limit):
    """
    Takes a list of weights, length of list, and a weight limit.
    Returns the 2 weights' indices that add to the limit,
    in reverse order. (higher index returned first)

    Returns None if no two are found.

    Overall runtime is approximately O(n)
    """
    # Create a blank dictionary
    d = {}

    # Store values of weights in dict (in lists in case of duplicates)
    # key = weight, value = index in list
    for i, w in enumerate(weights):  # O(n) over weights
        # Initialize list if weight not already in dict
        if w not in d:
            d[w] = []
        # Insert value at top of list
        d[w].insert(0, i)

    # Check to see if limit - weight exists in dict
    for k, v in d.items():  # O(n) over length of dict
        if limit - k in d:
            # If limit and k values are the same
            # Check for duplicate weights
            if d[limit-k] == v:
                # If only one index listed, then return None
                if len(v) == 1:
                    return None
                # Else, return the first two indices of the list
                return (v[0], v[1])
            # Return the first index from each list
            return (d[limit-k][0], v[0])

    return None
