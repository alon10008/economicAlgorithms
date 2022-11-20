import numpy as np
################ THIS ALGORITHM WORK FOR EVERY N PARTICIPANT ################
###### first index of the state is the number of items that given ######

close = {}                                           ### CLOSE LIST REPRESENT THE STATES THAT HAS ALREADY BEEN VISITED
items = np.array([10, 5, 5, 5, 12, 10, 2, 3, 5, 40]) ### LIST OF VLAUES OF ITEMS
counter = 1                                          ### COUNTER OF DFS
counterP = 1                                         ### COUNTER OF DFS_Prune


########## - check if state include in close list - ##########
def isInclude(key, dict):
    try:
        return dict[key]
    except:
        return False


########## - DFS SEARCH ALGORITHM WITH CLOSE LIST FOR PRUNING - ##########
def DFS_prune(state, best):
    global counterP
    global close
    close[str(state)] = True       # INSERT THE CURRENT STATE TO THE CLOSE LIST
    if state[0] == len(items):     # IF ALL THE ITEMS ARE GIVEN SO CHECK IF OPTIMAL
        return checkBest(state, best)
    itemIndex = state[0]           # THE NEXT ITEM
    for i in range(1, len(state)):  # CHECK ALL STATES
        s = np.array(state)
        s[0] += 1
        s[i] += items[itemIndex]
        if isInclude(str(s), close):    # IF THE STATE WAS VISITED THEN SKIP IT
            continue
        b = DFS_prune(s, best)
        counterP += 1
        best = checkBest(b, best)
    return best


########## - DFS SEARCH ALGORITHM - ##########
def DFS(state, best):
    global counter
    if state[0] == len(items):  # IF ALL THE ITEMS ARE GIVEN SO CHECK IF OPTIMAL
        return checkBest(state, best)
    itemIndex = state[0]              # THE NEXT ITEM
    for i in range(1, len(state)):    # CHECK ALL STATES
        counter += 1
        s = np.array(state)
        s[0] += 1
        s[i] += items[itemIndex]
        b = DFS(s, best)
        best = checkBest(b, best)
    return best


########## - CHECK WHICH STATE IS BETTER (egalitarian) - ##########
def checkBest(state, best):
    por = np.min(state[1:])      # TAKE THE MINIMUM VALUE OF EVERY STATE
    curr_best = np.min(best[1:])
    if por >= curr_best:          # CHECK WICH MINIMUM IS HIGHER
        return state
    return best


def printResult(title, best, counter):
    print("_____" + title + "_____")
    print("best state: " + str(best))
    print("number of state that was created: " + str(counter))


########## - CREATE THE START STATE AND CALL THE DFS FUNCTIONS - ##########
def main():
    start = np.array([0, 0, 0])  #CREATE START STATE OF TWO PARTICIPANTS AS REQUESTED
    best = DFS(start, start)
    printResult("DFS", best, counter)
    best = DFS_prune(start, start)
    printResult("DFS - Prune", best, counterP)
    print("\nnote:\n    The first index represent the number of items!")


if __name__ == "__main__":
    main()
