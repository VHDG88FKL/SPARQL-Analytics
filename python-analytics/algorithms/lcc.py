from collections import deque
from time import time
from parameters import GRAPH_NAME


# Loads a graph
def load_graph(data, limit=float('inf')):
    graph = {}
    with open(f'../datasets/{data}/{data}.v', 'r') as nodes:
        for node in nodes:
            graph[int(node)] = {'edges': deque(), 'neighbors': set()}
    with open(f'../datasets/{data}/{data}.e', 'r') as edges:
        count = 0
        for edge in edges:
            if count >= limit:
                break
            origin, destiny, weight = edge.strip().split(' ')
            graph[int(origin)]['edges'].append(int(destiny))
            graph[int(origin)]['neighbors'].add(int(destiny))
            graph[int(destiny)]['neighbors'].add(int(origin))
            count += 1
    return graph


# Local Clustering Coefficient
def lcc(graph, directed=True):
    coefficients = {}
    for x in graph:
        neighborhood = graph[x]['neighbors']
        counter = 0
        for neighbor in neighborhood:
            counter += len([x for x in graph[neighbor]['edges'] if x in
                            neighborhood])
        max_amount = len(neighborhood) * (len(neighborhood) - 1)
        if not directed:
            max_amount /= 2
        if max_amount:
            coefficients[x] = counter / max_amount
        else:
            coefficients[x] = float(0)
    return coefficients


def execute():
    start_loading = time()
    g = load_graph(GRAPH_NAME)
    end_loading = time()
    load_time = f"Loading Time: {end_loading - start_loading} Seconds " \
                f"({(end_loading - start_loading) / 60} Minutes) " \
                f"({(end_loading - start_loading) / 3600} Hours)"
    print(load_time)
    result = lcc(g)
    end_time = time()
    exec_time = f"Execution Time: {end_time - end_loading} Seconds " \
                f"({(end_time - end_loading) / 60} Minutes) " \
                f"({(end_time - end_loading) / 3600} Hours)"
    print(exec_time)
    with open(f'../results/LCC_{GRAPH_NAME}.txt', 'w') as file:
        file.write(load_time + '\n' + exec_time + '\n')
    with open(f'../outputs/LCC_{GRAPH_NAME}.txt', 'w') as file:
        for key, value in result.items():
            file.write(f"{key} {value}\n")
            print(key, value)
