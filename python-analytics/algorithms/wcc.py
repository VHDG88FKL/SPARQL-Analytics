from collections import deque
from time import time
from parameters import GRAPH_NAME


# Loads a graph
def load_graph(data, limit=float('inf')):
    graph = {}
    with open(f'../datasets/{data}/{data}.v', 'r') as nodes:
        for node in nodes:
            graph[int(node)] = {'neighbors': set(), 'group': 0}
    with open(f'../datasets/{data}/{data}.e', 'r') as edges:
        count = 0
        for edge in edges:
            if count >= limit:
                break
            line = edge.strip().split(' ')
            origin = int(line[0])
            destiny = int(line[1])
            graph[origin]['neighbors'].add(destiny)
            graph[destiny]['neighbors'].add(origin)
            count += 1
    return graph


# Weakly Connected Components (with DFS)
def wcc(graph):
    current_group = 1
    for v in graph:
        stack = deque([v])
        if not graph[v]['group']:
            graph[v]['group'] = current_group
            while stack:
                current = stack.pop()
                for v1 in graph[current]['neighbors']:
                    if not graph[v1]['group']:
                        graph[v1]['group'] = current_group
                        stack.append(v1)
            current_group += 1


def execute():
    start_loading = time()
    g = load_graph(GRAPH_NAME)
    end_loading = time()
    load_time = f"Loading Time: {end_loading - start_loading} Seconds " \
                f"({(end_loading - start_loading) / 60} Minutes) " \
                f"({(end_loading - start_loading) / 3600} Hours)"
    print(load_time)
    wcc(g)
    end_time = time()
    exec_time = f"Execution Time: {end_time - end_loading} Seconds " \
                f"({(end_time - end_loading) / 60} Minutes) " \
                f"({(end_time - end_loading) / 3600} Hours)"
    print(exec_time)
    with open(f'../results/WCC_{GRAPH_NAME}.txt', 'w') as file:
        file.write(load_time + '\n' + exec_time + '\n')
    with open(f'../outputs/WCC_{GRAPH_NAME}.txt', 'w') as file:
        for i in g:
            file.write(f"{i} {g[i]['group']}\n")
            print(i, g[i]['group'])
