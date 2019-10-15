# Python Analytics

Here are six algorithms written in Python that works with graphs from  [graphalytics](https://graphalytics.org/datasets). The algorithms that are implemented:

- Bread First Search (BFS)
- Weakly Connected Components (WCC)
- Page Rank (PR)
- Single-Source Shortest Path implemented with Dijkstra (SSSP)
- Local Clustering Coefficient (LCC)
- Community Detection Using Label Propagation (CDLP)

## Setting parameters

Before you run the algorithms make sure of change the parameters in `parameters.py` file:

- GRAPH_NAME: Describes the name of the graph that you want to execute the algorithm. The files of the graph must be on datasets/GRAPH_NAME and  the files GRAPH_NAME.e and GRAPH_NAME.v must be exists in that folder.

- MAX_ITERATIONS : Describes the max iterations that PR and CDLP must do.

- START_NODE : Describes the initial node for BFS.

- DAMPING_VALUE : Describes the dumping value for PR.

- INITIAL_PR : Describes the initial page rank of the nodes before exectute PR.

- SOURCE_NODE : Describes the initial node for SSSP.

- DESTINATION_NODE: Describes the destiny node for SSSP.


## Runing algorithms

For run the algorithms, you have to run the `main.py` file (That exectutes the six algorithms) in the folder `algorithms`.

The output will be saved in `output` folder. The time of execution will be saved in `result` folder.