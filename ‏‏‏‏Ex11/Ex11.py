import doctest


################# QUESTION - 1 #################


def remove_participants(preferences, cycle):   ### remove all the participants that got a house
    for i in range(len(cycle) - 1):
        preferences[cycle[i]] = None
    for per in preferences:
        for i in range(len(cycle) - 1):
            if per is not None:
                per.remove(cycle[i])
    return preferences


def get_start_index(preferences):   ## the first index not None
    i = 0
    for pre in preferences:
        if pre is not None:
            return i
        i += 1
    return -1                       ## if all None return -1


def find_trading_cycle(preferences):
    cycle = []
    start = get_start_index(preferences)  ## the first index not None
    if start == -1:
        return None
    cycle.append(start)
    current = start
    while True:             ## Every step of the algorithm must find a cycle or return empty list at start
        current = preferences[current][0]
        cycle.append(current)
        last_ind = len(cycle) - 1
        first_ind = cycle.index(current)
        if first_ind != last_ind:
            return cycle[first_ind:]


def top_trading_cycle(preferences):
    ans = []
    cycle = find_trading_cycle(preferences)
    while cycle is not None:
        ans.append(cycle)
        preferences = remove_participants(preferences, cycle)
        cycle = find_trading_cycle(preferences)
    return ans


def TEST():
    """
    >>> top_trading_cycle([[0]])
    [[0, 0]]

    >>> top_trading_cycle([[2, 1, 0, 3], [0, 1, 3, 2], [3, 2, 0, 1], [0, 2, 1, 3]])
    [[0, 2, 3, 0], [1, 1]]

    >>> top_trading_cycle([[2, 1, 0, 3], [2, 1, 3, 0], [3, 2, 0, 1], [1, 2, 0, 3]])
    [[2, 3, 1, 2], [0, 0]]

    >>> top_trading_cycle([[0, 1, 2], [1, 2, 0], [2, 0, 1]])
    [[0, 0], [1, 1], [2, 2]]

    >>> top_trading_cycle([[1, 0, 2, 3], [3, 1, 0, 2], [0, 3, 2, 1],[2, 0, 1, 3]])
    [[0, 1, 3, 2, 0]]

    >>> top_trading_cycle([[1, 2, 3, 0], [2, 3, 0, 1], [3, 0, 1, 2], [0, 1, 2, 3]])
    [[0, 1, 2, 3, 0]]

    >>> top_trading_cycle([[1, 2, 3, 0], [0, 3, 2, 1], [3, 0, 1, 2], [2, 1, 0, 3]])
    [[0, 1, 0], [2, 3, 2]]

    >>> top_trading_cycle([[0, 1, 2, 3], [1, 2, 3, 0], [2, 3, 0, 1], [3, 0, 1, 2]])
    [[0, 0], [1, 1], [2, 2], [3, 3]]

    >>> top_trading_cycle([[0, 1, 2, 3], [2, 1, 3, 0], [1, 3, 0, 2], [3, 0, 1, 2]])
    [[0, 0], [1, 2, 1], [3, 3]]

    >>> top_trading_cycle([[0, 1, 2, 3], [2, 1, 3, 0], [0, 3, 1, 2], [2, 0, 1, 3]])
    [[0, 0], [2, 3, 2], [1, 1]]

    >>> top_trading_cycle([[1, 2, 3, 4, 5, 0], [2, 3, 4, 5, 0, 1], [3, 4, 5, 0, 1, 2], [4, 5, 0, 1, 2, 3], [5, 0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5]])
    [[0, 1, 2, 3, 4, 5, 0]]

    >>> top_trading_cycle([[3, 1, 2, 3], [3, 1, 2, 0], [0, 3, 1, 2], [3, 0, 1, 2]])
    [[3, 3], [1, 1], [0, 2, 0]]
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
