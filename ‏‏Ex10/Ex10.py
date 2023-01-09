import numpy as np
import math


############# - CHECK IF THE RESULT IS EQUAL TO FAIR SHARE - #############
def checkDivision(group_counter, total_budget, result):
    citizen_num = group_counter.sum()
    fair = group_counter * (total_budget / citizen_num)
    diff = np.abs(result - fair)
    sum_of_diff = diff.sum()
    return sum_of_diff < 0.00000000001   # IN SOME CASES THE RESULT IS FOR EXAMPLE 20.000000000000004 INSTEAD OF 20


############# - BONUS QUESTION - #############
def group_fairness(total_budget, citizen_votes, result):
    group_counter = np.zeros_like(citizen_votes[0])
    citizen_votes = np.array(citizen_votes)
    for votes in citizen_votes:
        isOneSubject = np.where(votes == total_budget)
        if len(isOneSubject[0]) != 1:
            return False
        group_counter[isOneSubject[0][0]] += 1
    return checkDivision(group_counter, total_budget, result)


def compute_budget(total_budget, citizen_votes):
    citizen_votes = np.array(citizen_votes)
    leng = len(citizen_votes[0])
    t = binary_search(citizen_votes, 0.5, total_budget, leng)
    return median_per_subject(citizen_votes, t, total_budget, leng)


############# - FIND t - #############
def binary_search(citizen_votes, t, c, leng):
    gap = 0.5
    while True:
        ans = median_per_subject(citizen_votes, t, c, leng)
        ans = np.array(ans)
        sum_of_med = ans.sum()
        if sum_of_med == c:
            return t
        if sum_of_med > c:
            t -= gap
        if sum_of_med < c:
            t += gap
        gap *= 0.5


############# - FIND MEDIAN FOE EVERY SUBJECT - #############
def median_per_subject(citizen_votes, t, c, leng):
    ans = []
    consts = get_consts_by_f(c, t, len(citizen_votes[:, 0]))
    for i in range(leng):
        subject = citizen_votes[:, i]
        subject = np.concatenate((subject, consts))
        ans.append(median(subject, len(subject)))
    return ans


############# - SIMPLE MEDIAN FUNCTION - #############
def median(subject, leng):
    subject = np.sort(subject)
    return subject[math.floor(leng / 2)]


############# - CREATE (N - 1) CONSTANTS - #############
def get_consts_by_f(c, t, leng):
    consts = []
    for i in range(1, leng):
        consts.append(f(c, i, t))
    return np.array(consts)


############# - LINEAR FUNCTION - #############
def f(c, i, t):
    return c * min(1, i * t)


def TEST_budget(total_budget, citizen_votes):
    print("###################################")
    result = compute_budget(total_budget, citizen_votes)
    print("Total Budget: " + str(total_budget))
    print("\u0332".join(" Citizen Votes"))
    for i in range(len(citizen_votes)):
        print("Citizen " + str(i) + " votes: " + str(citizen_votes[i]))
    print("\u0332".join(" Final Result"))
    print(result)
    print("###################################\n")


def print_fairness(ans):
    if ans:
        print("The division" + "\u0332".join(" IS") +" fair to groups!")
        return
    print("The division" + "\u0332".join(" IS - NOT") + " fair to groups!")


def TEST_group_fairness(total_budget, citizen_votes):
    print("###################################")
    result = compute_budget(total_budget, citizen_votes)
    print("Total Budget: " + str(total_budget))
    print("\u0332".join(" Final Result"))
    print(result)
    group_fairness(total_budget, citizen_votes, result)
    print_fairness(group_fairness(total_budget, citizen_votes, result))
    print("###################################\n")


def main():
    total_budget = 100
    citizen_votes = [[100, 0, 0],
                     [0, 0, 100]]
    TEST_budget(total_budget, citizen_votes)

    total_budget = 100
    citizen_votes = [[100, 0, 0],
                     [0, 0, 100],
                     [20, 50, 30],
                     [10, 20, 70]]
    TEST_budget(total_budget, citizen_votes)

    total_budget = 100
    citizen_votes = [[100, 0, 0],
                     [0, 0, 100],
                     [100, 0, 0],
                     [0, 0, 100],
                     [100, 0, 0],
                     [0, 0, 100],
                     [0, 100, 0]]
    TEST_budget(total_budget, citizen_votes)

    total_budget = 60
    citizen_votes = [[60, 0, 0],
                     [0, 60, 0],
                     [0, 0, 60],
                     [60, 0, 0],
                     [60, 0, 0],
                     [0, 60, 0]]
    TEST_budget(total_budget, citizen_votes)

################# - FAIR TO GROUPS - #################
    print("\nFAIR TO GROUPS")
    total_budget = 100
    citizen_votes = [[100, 0, 0],
                     [0, 0, 100],
                     [100, 0, 0],
                     [0, 0, 100],
                     [100, 0, 0],
                     [0, 0, 100],
                     [0, 100, 0],
                     [100, 0, 0],
                     [0, 0, 100],
                     [0, 100, 0]]
    TEST_group_fairness(total_budget, citizen_votes)

    total_budget = 100
    citizen_votes = [[100, 0, 0],
                     [0, 0, 100],
                     [100, 0, 0],
                     [0, 0, 100],
                     [100, 0, 0],
                     [0, 0, 100],
                     [0, 50, 50],
                     [100, 0, 0],
                     [0, 0, 100],
                     [0, 100, 0]]
    TEST_group_fairness(total_budget, citizen_votes)

    total_budget = 60
    citizen_votes = [[60, 0, 0],
                     [0, 60, 0],
                     [0, 0, 60],
                     [0, 0, 60],
                     [60, 0, 0],
                     [0, 60, 0]]
    TEST_group_fairness(total_budget, citizen_votes)

    total_budget = 60
    citizen_votes = [[60, 0, 0],
                     [20, 20, 20],
                     [0, 0, 60],
                     [0, 0, 60],
                     [60, 0, 0],
                     [0, 60, 0]]
    TEST_group_fairness(total_budget, citizen_votes)

    total_budget = 60
    citizen_votes = [[60, 0, 0],
                     [0, 60, 0],
                     [0, 0, 60],
                     [60, 0, 0],
                     [60, 0, 0],
                     [0, 60, 0]]
    TEST_group_fairness(total_budget, citizen_votes)

    total_budget = 100
    citizen_votes = [[100, 0, 0],
                     [0, 0, 100],
                     [100, 0, 0],
                     [0, 0, 100],
                     [100, 0, 0],
                     [0, 0, 100],
                     [0, 100, 0]]
    TEST_group_fairness(total_budget, citizen_votes)


if __name__ == "__main__":
    main()
