import cvxpy as cvx


##################### - QUESTION - 3 - #####################


def buildVarDict(subjects, variables):
    dict = {}
    i = 0
    for sub in subjects:
        dict[sub] = variables[i]
        i += 1
    return dict


def build_utilities(preferences, dict):
    utilities = []
    for pref in preferences:
        u = None
        for p in pref:
            if u is None:
                u = dict[p]
                continue
            u += dict[p]
        utilities.append(u)
    return utilities


def printResult(utility_values, variables, dict, share, prefrences):
    print("BUDGET", end=": ")
    first = True
    for key, var in dict.items():
        if first:
            print(str(key) + "=" + str(var.value), end="")
            first = False
        else:
            print(", " + str(key) + "=" + str(var.value), end="")
    print()
    i = 0
    for pref in prefrences:
        print("Citizen " + str(i) + ": gives", end=" ")
        length = len(pref)
        j = 1
        if length == 1:
            print((share * dict[pref[0]].value) / utility_values[i], end=" to " + str(pref[0]))
        else:
            for p in pref:
                if length == j:
                    print((share * dict[p].value) / utility_values[i], end=" to " + str(p))
                    break
                if j == (length - 1):
                    print((share * dict[p].value) / utility_values[i], end=" to " + str(p) + " and ")
                    j += 1
                    continue
                print((share * dict[p].value) / utility_values[i], end=" to " + str(p) + ", ")
                j += 1
        print()
        i += 1
    print()


def Nash_budget(total, subjects, preferences):
    share = total / len(preferences)
    variables = cvx.Variable(len(subjects))
    dict = buildVarDict(subjects, variables)
    utilities = build_utilities(preferences, dict)
    sum_of_logs = cvx.sum([cvx.log(u) for u in utilities])
    positivity = [v >= 0 for v in variables]
    max_sum = [cvx.sum(variables) == total]
    problem = cvx.Problem(cvx.Maximize(sum_of_logs), constraints=max_sum+positivity)
    problem.solve()
    utility_values = [u.value for u in utilities]
    printResult(utility_values, variables, dict, share, preferences)


def main():

    total = 500
    subjects = ['a', 'b', 'c', 'd']
    preferences = [['a', 'b'],
                   ['a', 'c'],
                   ['a', 'd'],
                   ['b', 'c'],
                   ['a']]
    Nash_budget(total, subjects, preferences)

    preferences = [['b', 'a'],
                   ['c', 'a'],
                   ['d', 'a'],
                   ['c', 'b'],
                   ['a']]
    Nash_budget(total, subjects, preferences)

    preferences = [['b', 'd'],
                   ['a', 'c'],
                   ['a', 'd'],
                   ['b', 'c'],
                   ['a']]
    Nash_budget(total, subjects, preferences)

    subjects = ["Security", "Health", "Education", "Infrastructures"]
    preferences = [["Security", "Health"],
                   ["Security", "Education"],
                   ["Security", "Infrastructures"],
                   ["Health", "Education"],
                   ["Security"]]
    Nash_budget(total, subjects, preferences)

    total = 1_200
    preferences = [["Health", "Education", "Infrastructures"],
                   ["Infrastructures"],
                   ["Security", "Education"],
                   ["Health"],
                   ["Security", "Health"],
                   ["Security", "Education"]]
    Nash_budget(total, subjects, preferences)


if __name__ == "__main__":
    main()
