#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Takes input of tickets (from class Ticket)
    Returns correct order of flights, given "NONE" indicating
    First source and final destination.

    Overall runtime is approximately O(2n)
    """
    # Create empty dict
    d = {}

    # Input tickets into dictionary
    # key = source, value = destination
    for t in tickets:  # O(n) over amount of tickets
        d[t.source] = t.destination

    # Initialize empty route
    route = []

    # Begin route with first flight
    route.append(d["NONE"])

    # Generate loop to complete route
    for i in range(1, length):  # O(n) over amount of tickets
        # Use the most recently added destination to find the next
        route.append(d[route[i-1]])

    return route
