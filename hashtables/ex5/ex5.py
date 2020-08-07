# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Create empty dictionary
    d = {}

    # Iterate through files to store in dict
    # key = file name, value = full file path
    for f in files:  # O(n) over files
        # Use "/" as split to get filename
        filename = f.split("/")[-1]
        d[filename] = f

    # Generate empty list for results
    results = []

    # Iterate over queries to see which are present in dict
    for q in queries:
        # If query in dict, append filepath to results
        if q in d:
            results.append(d[q])

    return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
