from enum import Enum
import random


################ QUESTION - 2 ################


class BloodType(Enum):
    O = 0
    A = 1
    B = 2
    AB = 3


def calculate_match_event():
    counter = 0
    blood_types = list(BloodType)
    for sick in blood_types:
        for donor in blood_types:
            if isMatch(sick, donor):
                counter += 1
    return counter


def calculate_match_event_pair(altruism):
    counter = 0
    blood_types = list(BloodType)
    for sick in blood_types:
        for donor in blood_types:
            if isMatch(sick, donor):
               counter += 16
            else:
                counter += pair_match(sick, donor, altruism)
    return counter


def pair_match(sick_1, donor_1, altruism):
    counter = 0
    blood_types = list(BloodType)
    for sick_2 in blood_types:
        for donor_2 in blood_types:
            if not altruism and isMatch(sick_2, donor_2):
                continue
            if isMatch(sick_1, donor_2) and isMatch(sick_2, donor_1):
                counter += 1
    return counter


def isMatch(sick, donor):
    if sick is BloodType.AB:
        return True
    if donor is BloodType.O:
        return True
    if sick is donor:
        return True
    return False


def getRandomPair():
    lst = list(BloodType)
    return lst[random.randint(0, 3)], lst[random.randint(0, 3)]


def match_counter(trials):
    counter = 0
    for i in range(trials):
        sick, donor = getRandomPair()
        if isMatch(sick, donor):
            counter += 1
    return counter


def pair_match_counter(trials, altruism):
    counter = 0
    for i in range(trials):
        sick1, donor1 = getRandomPair()
        sick2, donor2 = getRandomPair()
        if isPairMatch(sick1, donor1, sick2, donor2, altruism):
            counter += 1
    return counter


def isPairMatch(sick1, donor1, sick2, donor2, altruism):
    if isMatch(sick1, donor1):
        return True
    if not altruism and isMatch(sick2, donor2):
        return False
    return isMatch(sick1, donor2) and isMatch(sick2, donor1)


def successMatchCounter(trials):
    counter = 0
    for i in range(trials):
        sick, donor = getRandomPair()
        if isMatch(sick, donor):
            counter += 1
    return counter


def printResult(trials):
    print("\u0332".join(" Probabilty that the donor's kidney match without cycles"))
    print("All option: 4^2 = 16 (simple combinatorics)")
    match_event = calculate_match_event()
    print("Number of matches: " + str(match_event) + " (simple function that tries all options)")
    print("Probability: " + str(match_event / 16))
    print("Performs " + str(f'{trials:n}') + " random trials:")
    success = successMatchCounter(trials)
    print("Success: " + str(success))
    print("Ratio: " + str(success / trials))

    print("\n" + "\u0332".join(" Probabilty that the donor's kidney match with cycles"))
    print("All option: 4^4 = 256 (simple combinatorics)")

    print("\nAltruism")
    match_event = calculate_match_event_pair(True)
    print("Number of matches: " + str(match_event) + " (simple function that tries all options)")
    print("Probability: " + str(match_event / 256))
    print("Performs " + str(f'{trials:n}') + " random trials:")
    success = pair_match_counter(trials, True)
    print("Success: " + str(success))
    print("Ratio: " + str(success / trials))

    print("\nEgoism")
    match_event = calculate_match_event_pair(False)
    print("Number of matches: " + str(match_event) + " (simple function that tries all options)")
    print("Probability: " + str(match_event / 256))
    print("Performs " + str(f'{trials:n}') + " random trials:")
    success = pair_match_counter(trials, False)
    print("Success: " + str(success))
    print("Ratio: " + str(success / trials))

    print("\nnotes:")
    print("* There are two approaches:")
    print("\t1. Altruism - The donor try to find cycle so he might save two people.")
    print("\t2. Egoism - The donor's only interest is to save his/her loved one.")
    print("* In both approaches when there is a match between donor1 and sick1")
    print("  it counts as match without even check the other pair.")
    print("*  - OBVIOUSLY - THE MORE TRIALS WE PERFORM THE RATIO GET CLOSER TO THE ACTUAL PROBABILITY (LLN)")


def main():
    printResult(100_000)


if __name__ == "__main__":
    main()
