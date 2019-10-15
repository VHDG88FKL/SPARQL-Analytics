# Python Analytics :snake:

Here are six algorithms coded in Python that work with the datasets from  [graphalytics](https://graphalytics.org/datasets). The following algorithms were implemented:

- Breadth First Search (BFS)
- Weakly Connected Components (WCC)
- Page Rank (PR)
- Single-Source Shortest Path w/ Dijkstra (SSSP)
- Local Clustering Coefficient (LCC)
- Community Detection Using Label Propagation (CDLP)

## Setting Parameters

Before running the algorithms make sure to check the following parameters in the `parameters.py` file:

- GRAPH_NAME: Describes the name of the graph that you want the algorithm to be executed on. The graph files must be on `datasets/GRAPH_NAME` (GRAPH_NAME.e and GRAPH_NAME.v must exist inside that folder).

- MAX_ITERATIONS : Describes the max number of iterations that PR and CDLP can do.

- START_NODE : Describes the source node for BFS.

- DAMPING_VALUE : Describes the damping value for PR.

- INITIAL_PR : Describes the initial Page Rank of each node before executing PR.

- SOURCE_NODE : Describes the source node for SSSP.

- DESTINATION_NODE: Describes the destiny node for SSSP.


## Running The Algorithms

To execute all the algorithms you have to run the `main.py` file in the `algorithms` folder.

The outputs will be saved in the `output` folder. The execution times will be saved in the `result` folder.