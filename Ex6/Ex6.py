import networkx as nx

##################### - QUESTION - 3 - #####################


########### - build the graph and look for cycle - ###########
def find_cycle_in_consumption_graph(allocation):
    graph = buildGraph(allocation)
    cycle = getCycle(graph)
    print(cycle)


########### - find the cycle in the graph - ###########
def getCycle(graph):
    try:
        cycle = nx.find_cycle(graph)
    except:
        cycle = "There is no cycle in the graph!"   ### if catch exception there is no cycle in graph!
    finally:
        return cycle


########### - build the graph using the cunsumption graph - ###########
def buildGraph(division):
    graph = nx.Graph()
    for i in range(len(division)):
        graph.add_node("p" + str(i + 1))
        for j in range(len(division[i])):
            if division[i][j]:
                graph.add_edge("p" + str(i + 1), "item" + str(j + 1))
    return graph


def main():
    division = [[1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 1, 0],
                [1, 0, 1, 0, 0]]
    find_cycle_in_consumption_graph(division)
    division = [[1, 0.5, 0, 0, 0],
                [0, 0.5, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 1, 0],
                [1, 0, 1, 0, 0]]
    find_cycle_in_consumption_graph(division)
    division = [[0.5, 0.5, 0, 0, 0],
                [0.5, 0.5, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 1, 0],
                [1, 0, 1, 0, 0]]
    find_cycle_in_consumption_graph(division)
    division = [[0.2, 0.2, 0.2, 0.2, 0.2],
                [0.2, 0.2, 0.2, 0.2, 0.2],
                [0.2, 0.2, 0.2, 0.2, 0.2],
                [0.2, 0.2, 0.2, 0.2, 0.2],
                [0.2, 0.2, 0.2, 0.2, 0.2]]
    find_cycle_in_consumption_graph(division)


if __name__ == "__main__":
    main()
