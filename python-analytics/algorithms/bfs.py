from collections import deque
from time import time
from parameters import START_NODE, GRAPH_NAME, DIRECTED


# Loads a graph
def load_graph(data, limit=float('inf'), directed=True):
    graph = {}
    with open(f'../datasets/{data}/{data}.v', 'r') as nodes:
        for node in nodes:
            graph[int(node)] = {'neighbors': deque(), 'id': int(node),
                                'visited': False, 'distance': None}
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


# Breadth First Search
def bfs(graph, start_node):
    nodes = deque([start_node])
    graph[start_node]['distance'] = 0
    graph[start_node]['visited'] = True
    while nodes:
        node = nodes.popleft()
        for v in filter(lambda x: not graph[x]['visited'], graph[node]['neighbors']):
            graph[v]['distance'] = graph[node]['distance'] + 1
            graph[v]['visited'] = True
            nodes.append(v)
      

def execute():
    start_loading = time()
    g = load_graph(GRAPH_NAME, directed=DIRECTED)
    end_loading = time()
    load_time = f"Loading Time: {end_loading - start_loading} Seconds " \
                f"({(end_loading - start_loading) / 60} Minutes) " \
                f"({(end_loading - start_loading) / 3600} Hours)"
    print(load_time)
    bfs(g, START_NODE)
    end_time = time()
    exec_time = f"Execution Time: {end_time - end_loading} Seconds " \
                f"({(end_time - end_loading) / 60} Minutes) " \
                f"({(end_time - end_loading) / 3600} Hours)"
    print(exec_time)
    with open(f'../results/BFS_{GRAPH_NAME}.txt', 'w') as file:
        file.write(load_time + '\n' + exec_time + '\n')
    with open(f'../outputs/BFS_{GRAPH_NAME}.txt', 'w') as file:
        for n in g:
            if g[n]['distance'] is not None:
                file.write(f"{n} {g[n]['distance']}\n")
                print(n, g[n]['distance'])
            else:
                file.write(f"{n} infinity\n")
                print(n, 'infinity')
