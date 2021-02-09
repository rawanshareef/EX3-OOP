_EX3_
### _Introduction_:
 

**This project presents a directed weighted graph. 
The goal of this project is to implement a directional weighted graph using python.
 directed weighted graph is a graph that has a source node, a destination node and an edge that connect between them.
 in this part we have 2 classes that implemented 2 interfaces:
 DiGraph.py implements GraphInterface.py - This class represent a directed weighted graph.
This class includes a NodeData class that represents a single node in a graph. Each node has a unique key, tag and location. 
GraphAlgo.py implement GraphAlgoInterface - in this class we holds a directed weighted graph, and we do actions and algorithms on him This class includes a NodeAlgo class, we add this class in order to save the father for each node.**

### Project functions:
_**DiGraph:**_

**def v_size(self) -> int:** returns the number of nodes in the graph.

**def e_size(self) -> int:** returns the number of edges in the graph.

**def get_all_v(self) -> dict:** return a dictionary of all the nodes in the Graph. 

**def all_in_edges_of_node(self, id1: int) -> dict:** return a dictionary of all the nodes connected to (into) id1.

**def all_out_edges_of_node(self, id1: int) -> dict:** return a dictionary of all the nodes connected from id1.

**def get_mc(self) -> int:** returns the current version of this graph, Mode Count - for testing changes in the graph.

**def add_edge(self, id1: int, id2: int, weight: float) -> bool:** adds an edge to the graph. 
return True if the edge was added successfully, else return False. if the edge already exists or one of the nodes dose not exists the functions will do nothing.

**def add_node(self, node_id: int, pos: tuple = None) -> bool:** adds a node to the graph.
return True if the node was added successfully, else return False. if the node id already exists the node will not be added.
  
**def remove_node(self, node_id: int) -> bool:** removes a node from the graph.
retern True if the node was removed successfully, else return False. if the node id does not exists the function will do nothing.
  
**def remove_edge(self, node_id1: int, node_id2: int) -> bool:** removes an edge from the graph.
return True if the edge was removed successfully, else return False. If such an edge does not exists the function will do nothing


_**GraphAlgo:**_

**def get_graph(self) -> GraphInterface:** return the directed graph on which the algorithm works on.

**def shortest_path(self, id1: int, id2: int) -> (float, list):** check the shortest path from node id1 to node id2 using Dijkstra's Algorithm.
  this method save the father to each node and in this way save a path of nodes between id1 and id2.
  return the distance of the path, a list of the nodes ids that the path goes through.
  if there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[]).
  
**def connected_component(self, id1: int) -> list:** finds the Strongly Connected Component(SCC) that node id1 is a part of. This method based on BFS Algorithm.
the method get a node id and find his SCC.
in order to do this, we check which nodes id1 can arrive, and after this, we check the nodes that can arrive to id1.
Finally, we compare between the 2 lists and We return the common nodes.
return a list of nodes in the SCC.
if the graph is None or id1 is not in the graph, the function should return an empty list [].

 **def connected_components(self) -> List[list]:** finds all the Strongly Connected Component(SCC) in the graph.
 this method pass all the nodes in the graph and find the SCC for each node. this method use connected_component.
 return The list[list] for all SCC in the graph. if the graph is None the function should return an empty list [].    
        
**def load_from_json(self, file_name: str) -> bool:** loads a graph from a json file. 
  return True if the loading was successful, else return False.
  
**def save_to_json(self, file_name: str) -> bool:** saves the graph in JSON format to a file
 return True if the save was successful, else return False.
 
**def plot_graph(self) -> None:** plots the graph.
  if the nodes have a position, the nodes will be placed there. Otherwise, they will be placed in a random but elegant manner.


