def finder(files, queries):
    """
    Takes input of filepaths and filename queries
    Outputs full filepaths of any filepath matching given query.

    Overall runtime is O(n).
    """
    # Create empty dictionary
    d = {}

    # Iterate through files to store in dict
    # key = file name, value = full file path
    for f in files:  # O(n) over files
        # Use "/" as split to get filename
        filename = f.split("/")[-1]
        # If filename not yet in d, initialize empty list
        if filename not in d:
            d[filename] = []
        d[filename].append(f)

    # Generate empty list for results
    results = []

    # Iterate over queries to see which are present in dict
    for q in queries:  # O(n) over queries
        # If query in dict, add filepath(s) to results
        if q in d:
            results.extend(d[q])

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
