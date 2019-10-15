from collections import deque
from time import time
from parameters import (INITIAL_PR, DAMPING_VALUE,
                        MAX_ITERATIONS, GRAPH_NAME, DIRECTED)


# Loads a graph
def load_graph(data, limit=float('inf'), directed=True):
    graph = {}
    with open(f'../datasets/{data}/{data}.v', 'r') as nodes:
        for node in nodes:
            graph[int(node)] = {'outlinks': deque(), 'backlinks': deque(),
                                'pr_1': INITIAL_PR, 'pr_2': INITIAL_PR}
    with open(f'../datasets/{data}/{data}.e', 'r') as edges:
        count = 0
        for edge in edges:
            if count >= limit:
                break
            line = edge.strip().split(' ')
            origin = int(line[0])
            destiny = int(line[1])
            graph[origin]['outlinks'].append(destiny)
            graph[destiny]['backlinks'].append(origin)
            if not directed:
                graph[origin]['backlinks'].append(destiny)
                graph[destiny]['outlinks'].append(origin)
            count += 1
    return graph


# Page Rank calculation
def calculate_pr_value(graph, node, switch):
    # The switch parameter is for alternating between the values of pr from
    # the current and last iteration
    value = 1 - DAMPING_VALUE
    for neighbor in node['backlinks']:
        if switch:
            value += DAMPING_VALUE * (graph[neighbor]['pr_1'] /
                                      len(graph[neighbor]['outlinks']))
        else:
            value += DAMPING_VALUE * (graph[neighbor]['pr_2'] /
                                      len(graph[neighbor]['outlinks']))
    if switch:
        node['pr_2'] = value
    else:
        node['pr_1'] = value


# Page Rank
def pr(graph):
    iterations = 0
    while iterations < MAX_ITERATIONS:
        for node in graph:
            calculate_pr_value(graph, graph[node], iterations % 2)
        iterations += 1


def execute():
    start_loading = time()
    g = load_graph(GRAPH_NAME, directed=DIRECTED)
    end_loading = time()
    load_time = f"Loading Time: {end_loading - start_loading} Seconds " \
                f"({(end_loading - start_loading) / 60} Minutes) " \
                f"({(end_loading - start_loading) / 3600} Hours)"
    print(load_time)
    pr(g)
    end_time = time()
    exec_time = f"Execution Time: {end_time - end_loading} Seconds " \
                f"({(end_time - end_loading) / 60} Minutes) " \
                f"({(end_time - end_loading) / 3600} Hours)"
    print(exec_time)
    with open(f'../results/PR_{GRAPH_NAME}.txt', 'w') as file:
        file.write(load_time + '\n' + exec_time + '\n')
    with open(f'../outputs/PR_{GRAPH_NAME}.txt', 'w') as file:
        for vertex in g:
            if MAX_ITERATIONS % 2:
                file.write(f"{vertex} {g[vertex]['pr_2']}\n")
                print(vertex, g[vertex]['pr_2'])
            else:
                file.write(f"{vertex} {g[vertex]['pr_1']}\n")
                print(vertex, g[vertex]['pr_1'])
