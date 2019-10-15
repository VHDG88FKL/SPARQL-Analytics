from collections import deque
from time import time
from parameters import GRAPH_NAME, SOURCE_NODE, DIRECTED, DESTINATION_NODE


# Loads a graph
def load_graph(data, limit=float('inf'), directed=True):
    graph = {}
    with open(f'../datasets/{data}/{data}.v', 'r') as nodes:
        for node in nodes:
            graph[int(node)] = {'neighbors': deque(), 'visited': False,
                                'distance': float('inf'), 'previous': None}
    with open(f'../datasets/{data}/{data}.e', 'r') as edges:
        count = 0
        for edge in edges:
            if count >= limit:
                break
            line = edge.strip().split(' ')
            origin = int(line[0])
            destiny = int(line[1])
            graph[origin]['neighbors'].append(destiny)
            if not directed:
                graph[destiny]['neighbors'].append(origin)
            count += 1
    return graph


def get_path(graph, destination):
    if graph[destination]['previous']:
        path = deque()
        destiny = destination
        while destiny:
            path.appendleft(destiny)
            destiny = graph[destiny]['previous']
        return path, graph[destination]['distance']
    else:
        return None, 'infinity'


def update_distance(min_distance, distances):
    if min_distance in distances:
        return min_distance
    return min(distances.keys())


def choose_next_node(min_distance, distances):
    next_node = distances[min_distance].pop()
    if not distances[min_distance]:
        del distances[min_distance]
    return next_node


# Single-Source Shortest Path (with Dijkstra)
def sssp(graph, source, destination):
    distances = {0: deque([source])}
    graph[source]['distance'] = 0
    min_distance = 0
    current = source
    while distances and (current != destination):
        min_distance = update_distance(min_distance, distances)
        current = choose_next_node(min_distance, distances)
        graph[current]['visited'] = True
        for n in graph[current]['neighbors']:
            if not graph[n]['visited']:
                new_distance = graph[current]['distance'] + 1
                if new_distance < graph[n]['distance']: 
                    graph[n]['distance'] = new_distance
                    graph[n]['previous'] = current
                    if new_distance not in distances:
                        distances[new_distance] = deque()
                    distances[new_distance].append(n)
    return get_path(graph, destination)


def execute():
    start_loading = time()
    g = load_graph(GRAPH_NAME, directed=DIRECTED)
    end_loading = time()
    load_time = f"Loading Time: {end_loading - start_loading} Seconds " \
                f"({(end_loading - start_loading) / 60} Minutes) " \
                f"({(end_loading - start_loading) / 3600} Hours)"
    print(load_time)
    result = sssp(g, SOURCE_NODE, DESTINATION_NODE)
    end_time = time()
    exec_time = f"Execution Time: {end_time - end_loading} Seconds " \
                f"({(end_time - end_loading) / 60} Minutes) " \
                f"({(end_time - end_loading) / 3600} Hours)"
    print(exec_time)
    with open(f'../results/SSSP_{GRAPH_NAME}.txt', 'w') as file:
        file.write(load_time + '\n' + exec_time + '\n')
    with open(f'../outputs/SSSP_{GRAPH_NAME}.txt', 'w') as file:
        if result[0]:
            file.write(f"Path: {list(result[0])}, Distance: {result[1]}\n")
            print(list(result[0]), result[1])
        else:
            file.write(f"Path: Unreachable, Distance: {result[1]}\n")
            print(result[0], result[1])
