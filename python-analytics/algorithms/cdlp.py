from time import time
from parameters import MAX_ITERATIONS, GRAPH_NAME


# Loads a graph
def load_graph(data, limit=float('inf')):
    graph = {}
    with open(f'../datasets/{data}/{data}.v', 'r') as nodes:
        for node in nodes:
            graph[int(node)] = {'neighbors': set(),
                                'label': int(node)}
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


# Finds most common label
def find_most_common(list_labels):
    max_element = max(list_labels, key=list_labels.count)
    max_values = filter(
        lambda x: list_labels.count(x) == list_labels.count(max_element),
        list_labels)
    return min(max_values)


# Updates the label of a node
def update_label(graph, node):
    labels = list(map(lambda v: graph[v]['label'], graph[node]['neighbors']))
    if labels:
        graph[node]['label'] = find_most_common(labels)


# Community Detection Using Label Propagation
def cdlp(graph):
    iteration = 0
    while iteration < MAX_ITERATIONS:
        for node in graph:
            update_label(graph, node)
        iteration += 1


def execute():
    start_loading = time()
    g = load_graph(GRAPH_NAME)
    end_loading = time()
    load_time = f"Loading Time: {end_loading - start_loading} Seconds " \
                f"({(end_loading - start_loading) / 60} Minutes) " \
                f"({(end_loading - start_loading) / 3600} Hours)"
    print(load_time)
    cdlp(g)
    end_time = time()
    exec_time = f"Execution Time: {end_time - end_loading} Seconds " \
                f"({(end_time - end_loading) / 60} Minutes) " \
                f"({(end_time - end_loading) / 3600} Hours)"
    print(exec_time)
    with open(f'../results/CDLP_{GRAPH_NAME}.txt', 'w') as file:
        file.write(load_time + '\n' + exec_time + '\n')
    with open(f'../outputs/CDLP_{GRAPH_NAME}.txt', 'w') as file:
        for vertex in g:
            file.write(f"{vertex} {g[vertex]['label']}\n")
            print(vertex, g[vertex]['label'])
