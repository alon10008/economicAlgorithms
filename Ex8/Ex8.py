import numpy as np
import copy

##################### - QUESTION - 1 - #####################


def VCG(bidders):
    length = len(bidders[0])
    sumPerBidder = sumOfBidder(bidders, length)
    shareExclude = getShareExclude(bidders, length)
    sumExclude = getSumExclude(sumPerBidder, length)
    ItemsPerBidder = getItemsPerBidder(bidders, length)
    return printResult(sumPerBidder, shareExclude, sumExclude, ItemsPerBidder, length)


def printResult(sumPerBidder, shareExclude, sumExclude, ItemsPerBidder, length):
    result = getFinalResult(sumPerBidder, shareExclude, sumExclude, length)
    for i in range(length):
        print("\u0332".join(" Bidder number " + str(i)))
        print("Items: " + str(ItemsPerBidder[i]))
        print("Total offer: " + str(sumPerBidder[i]))
        print("Sum of values exclude bidder " + str(i) + ": " + str(sumExclude[i]))
        print("Sum of values of auction exclude bidder " + str(i) + ": " + str(shareExclude[i]))
        print("Final price: " + str(shareExclude[i]) + " - " + str(sumExclude[i]) + " = " + str(result[i]), end="\n\n")
    return result


def getItemsPerBidder(bidders, length):
    dict = buildDict(length)
    share = np.array(getShare(bidders))
    for i in range(length):
        dict[i] = str(np.where(share == i)[0]).replace("[", "").replace("]", "").replace(" ", ", ")
        if dict[i] == "":
            dict[i] = "none"
    return dict


def getFinalResult(sumPerBidder, shareExclude, sumExclude, length):
    dict = buildDict(length)
    for i in range(length):
        dict[i] = shareExclude[i] - sumExclude[i]
    return dict


def sumOfBidder(bidders, length):
    dict = buildDict(length)
    share = getShare(bidders)
    for i in range(length):
        bidderIndex = share[i]
        dict[bidderIndex] += bidders[bidderIndex, i]
    return dict


def getShareExclude(bidders, length):
    dict = buildDict(length)
    for i in range(length):
        dict[i] = sum(sumOfBidder(np.delete(bidders, i, 0), length).values())
    return dict


def getSumExclude(sumPerBidder, length):
    dict = buildDict(length)
    for i in range(length):
        dictCopy = copy.deepcopy(sumPerBidder)
        dictCopy[i] = 0
        dict[i] = sum(dictCopy.values())
    return dict


def getShare(bidders):
    winners = []
    for i in range(len(bidders[0])):
        winners.append(np.argmax(bidders[:, i]))
    return winners


def buildDict(length):
    ans = {}
    for i in range(length):
        ans[i] = 0
    return ans


def TEST(bidders):
    print("###################################")
    VCG(bidders)
    print("###################################\n")


def main():
    bidder0 = [80, 90]
    bidder1 = [70, 95]
    bidders = np.array([bidder0, bidder1])
    TEST(bidders)
    bidder0 = [1, 2, 3]
    bidder1 = [20, 401, 40]
    bidder2 = [300, 400, 500]
    bidders = np.array([bidder0, bidder1, bidder2])
    TEST(bidders)


if __name__ == "__main__":
    main()
