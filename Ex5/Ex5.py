import numpy as np

################################ --- QUESTION - 2 --- ################################


########### - check if the current state is 'organized' - ###########
def isOrderDivision(value_a, value_b, div_a, div_b):
    relation = value_a / value_b
    max_b = np.max(div_b * relation)
    div_a[div_a == 0] = np.inf
    min_a = np.min(div_a * relation)
    if min_a == np.inf:
        return False
    return (min_a - max_b) >= 0


########### - find the most valuable item that the other participant have - ###########
def findMax(value_a, value_b, div_a, div_b):
    while True:
        ind_a = np.argmax(value_a)
        if div_b[ind_a]:
            break
        value_a[ind_a] = 0
    while True:
        ind_b = np.argmax(value_b)
        if div_a[ind_b]:
            break
        value_b[ind_b] = 0
    if ind_a == ind_b:
        value_a[ind_a] = 0
        #value_b[ind_b] = 0
        return findMax(value_a, value_b, div_a, div_b)
    return ind_a, ind_b


########### - take half of the smaller item, used to create pareto improvement - ###########
def getAmount(div_a, div_b, ind_a, ind_b):
    if div_b[ind_a] < div_a[ind_b]:
        return div_b[ind_a] / 2
    return div_a[ind_b] / 2


########### - check if the current state is pareto optimal - ###########
def isParetoOptimal(value_a, value_b, div_a, div_b):
    if np.array_equal(value_a, value_b):
        return True
    if np.sum(div_a) == 0 or np.sum(div_b) == 0:
        return True
    return False


########### - give small chunk of the most valuable item that belong to the other participant - ###########
def getParetoImprovement(value_a, value_b, div_a, div_b):
    if isParetoOptimal(value_a, value_b, div_a, div_b): ### check if the current state is pareto optimal
        return "optimal"            ### if it is pareto optimal => by definition cant get pareto improvement
    ind_a, ind_b = findMax(np.array(value_a), np.array(value_b), np.array(div_a), np.array(div_b))
    amount = getAmount(np.array(div_a), np.array(div_b), np.array(ind_a), np.array(ind_b))
    div_a[ind_b] -= amount          #### re-divide the most valuable item of each participant
    div_b[ind_b] += amount
    div_b[ind_a] -= amount
    div_a[ind_a] += amount
    return [div_a, div_b]


########### - QUESTION 2 - ALGORITHM - ###########
########### - if the division is organized  return yes / else return pareto improvement of the current state - ###########
def question2(value_a, value_b, div_a, div_b):
    if isOrderDivision(np.array(value_a), np.array(value_b), np.array(div_a), np.array(div_b)):
        return "Yes"
    return getParetoImprovement(np.array(value_a), np.array(value_b), np.array(div_a), np.array(div_b))


def TEST(value_a, value_b, div_a, div_b, num):
    print("\n####################################################################")
    print("----------------------------- TEST " + str(num) + " -------------------------------")
    print("A - VALUES TABLE: " + str(value_a) + ", A's  SHARE: " + str(div_a))
    print("B - VALUES TABLE: " + str(value_b) + ", B's - SHARE: " + str(div_b))
    print("THE TOTAL VALUE OF A: " + str(np.sum(div_a * value_a)))
    print("THE TOTAL VALUE OF B: " + str(np.sum(div_b * value_b)))
    ans = question2(value_a, value_b, div_a, div_b)
    if ans == "Yes":
        print("THE DIVISION IS 'ORGANIZED'!")
    elif ans == "optimal":
        print("THE CURRENT STATE IS PARETO OPTIMAL! - THERE IS NO PARETO IMPROVEMENT")
    else:
        print("THE DIVISION ISN'T 'ORGANIZED'!")
        print("PARETO IMPROVEMENT OF THE CURRENT STATE:")
        print("THE NEW TOTAL VLUE OF A: " + str(np.sum(ans[0] * value_a)) + ", A's NEW SHARE:" + str(ans[0]))
        print("THE NEW TOTAL VLUE OF B: " + str(np.sum(ans[1] * value_b)) + ", B's NEW SHARE:" + str(ans[1]))

    print("--------------------------------------------------------------------")
    print("####################################################################\n")


########### - run simple examples of the algorithm - ###########
def main():
    value_a = np.array([40, 30, 20, 10], float)
    value_b = np.array([10, 20, 30, 40], float)
    div_a = np.array([1, 0, 0.4, 0.7], float)
    div_b = np.array([0, 1, 0.6, 0.3], float)
    TEST(value_a, value_b, div_a, div_b, 1)

    value_a = np.array([30, 30, 20, 20], float)
    value_b = np.array([30, 30, 20, 20], float)
    div_a = np.array([1, 1, 1, 1], float)
    div_b = np.array([0, 0, 0, 0], float)
    TEST(value_a, value_b, div_a, div_b, 2)

    value_a = np.array([20, 30, 20, 10], float)
    value_b = np.array([10, 20, 30, 40], float)
    div_a = np.array([0, 0, 0, 0], float)
    div_b = np.array([1, 1, 1, 1], float)
    TEST(value_a, value_b, div_a, div_b, 3)

    value_a = np.array([25, 25, 25, 25], float)
    value_b = np.array([25, 25, 25, 25], float)
    div_a = np.array([1, 0, 0, 1], float)
    div_b = np.array([0, 1, 1, 0], float)
    TEST(value_a, value_b, div_a, div_b, 4)

    value_a = np.array([40, 40, 10, 10], float)
    value_b = np.array([10, 10, 40, 40], float)
    div_a = np.array([0, 0.5, 1, 1], float)
    div_b = np.array([1, 1, 0, 1], float)
    TEST(value_a, value_b, div_a, div_b, 5)

    value_a = np.array([10, 20, 30, 50], float)
    value_b = np.array([50, 30, 20, 10], float)
    div_a = np.array([1, 1, 1, 0], float)
    div_b = np.array([0, 1, 1, 1], float)
    TEST(value_a, value_b, div_a, div_b, 6)


if __name__ == "__main__":
    main()
