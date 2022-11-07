class Agent:
    def __init__(self, options):
        self.options = options

    def value(self, option):
        return self.options[option]


def isParetoImprovement(agents, option1, option2):
    improvement = False
    for agent in agents:
        if agent.value(option2) > agent.value(option1):
            return False
        if agent.value(option2) < agent.value(option1):
            improvement = True
    return improvement


def isParetoOptimal(agents, option, allOptions):
    for opt in allOptions:
        if opt == option:
            continue
        if isParetoImprovement(agents, opt, option):
            return False
    return True


def TESTimprovement(agents, option1, option2):
    if isParetoImprovement(agents, option1, option2):
        print("Option " + str(option1) + " is PARETO improvement over option " + str(option2))
    else:
        print("Option " + str(option1) + " isn't PARETO improvement over option " + str(option2))


def TESToptimal(agents, option, allOptions):
    if isParetoOptimal(agents, option, allOptions):
        print("option " + str(option) + " is PARETO optimal!")
    else:
        print("option " + str(option) + " isn't PARETO optimal!")


ami = Agent([1, 2, 3, 4, 5])
tami = Agent([3, 1, 2, 5, 4])
rami = Agent([3, 5, 5, 1, 1])
agents = [ami, tami, rami]
allOptions = range(5)

print("############ - test pareto improvement - ############")
for opt1 in range(len(allOptions)):
    for opt2 in range(len(allOptions)):
        if opt1 == opt2:
            continue
        TESTimprovement(agents, opt1, opt2)



print("\n############ - test pareto optimal - ############")
for opt in range(len(allOptions)):
    TESToptimal(agents, opt, allOptions)
