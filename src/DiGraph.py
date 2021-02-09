from src.GraphInterface import GraphInterface


class NodeData:
    """ This class represents on a node in a directional weighted graph."""

    def __init__(self, key: int = None, tag: int = 0, pos: tuple = None):
        """method is similar to constructor in java. this method used to initialize the node state."""
        self.key = key
        self.tag = tag
        self.pos = pos

    def __repr__(self):
        """ function returns a printable representation of the node.
        @return: node string"""
        return f'NodeData: {self.key}, tag={self.tag}, pos= {self.pos}'


class DiGraph(GraphInterface):
    """This class represents the interface of a directed weighted graph."""

    def __init__(self):
        """method is similar to constructor in java. this method used to initialize the graph state."""
        self.nodesMap = {}
        self.outMap = {}
        self.inMap = {}
        self.mc = 0
        self.edgesSize = 0

    def v_size(self) -> int:
        """ returns the number of nodes in the graph.
        @return: nodes number int"""
        return len(self.nodesMap)

    def e_size(self) -> int:
        """returns the number of edges in the graph.
        @return: edges number int"""
        return self.edgesSize

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph. each node is represented using a pair (key, node_data)
        @return: nodes dict"""
        return self.nodesMap

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) id1 ,
         each node is represented using a pair (key, weight)
         @return: in nodes dict """
        if (self.nodesMap.get(id1) is not None):
            return self.inMap.get(id1)
        else:
            return {}

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from id1 , each node is represented using a pair(key, weight)
        @return: out nodes dict"""
        if (self.nodesMap.get(id1) is not None):
            return self.outMap.get(id1)
        else:
            return {}

    def get_mc(self) -> int:
        """returns the current version of this graph, Mode Count - for testing changes in the graph.
        return: mc int"""
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """ adds an edge to the graph.
            @param id1: The start node of the edge
            @param id2: The end node of the edge
            @param weight: The weight of the edge
            @return: True if the edge was added successfully, False o.w.
            Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing"""
        if (self.nodesMap.get(id1) is not None) and (self.nodesMap.get(id2) is not None) and (id1 is not id2) and (
                weight >= 0):
            if id2 not in self.outMap.get(id1) and id1 not in self.inMap.get(id2):
                self.outMap[id1][id2] = weight
                self.inMap[id2][id1] = weight
                self.edgesSize = self.edgesSize + 1
                self.mc = self.mc + 1
                return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """ adds a node to the graph.
            @param node_id: The node ID
            @param pos: The position of the node
            @return: True if the node was added successfully, False o.w.
            Note: if the node id already exists the node will not be added"""
        if self.nodesMap.get(node_id) is not None:
            return False
        else:
            node = NodeData(key=node_id, pos=pos)
            self.nodesMap[node_id] = node
            self.inMap[node_id] = {}
            self.outMap[node_id] = {}
            self.mc = self.mc + 1
            return True

    def remove_node(self, node_id: int) -> bool:
        """ removes a node from the graph.
            @param node_id: The node ID
            @return: True if the node was removed successfully, False o.w.
            Note: if the node id does not exists the function will do nothing"""
        if self.nodesMap.get(node_id) is not None:
            for i in list(self.all_in_edges_of_node(node_id)):
                self.remove_edge(i, node_id)
                self.mc = self.mc - 1
            for j in list(self.all_out_edges_of_node(node_id)):
                self.remove_edge(node_id, j)
                self.mc = self.mc - 1
            del self.nodesMap[node_id]
            self.mc = self.mc + 1
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """ removes an edge from the graph.
            @param node_id1: The start node of the edge
            @param node_id2: The end node of the edge
            @return: True if the edge was removed successfully, False o.w.
            Note: If such an edge does not exists the function will do nothing"""
        if (self.nodesMap.get(node_id1) is not None) and (self.nodesMap.get(node_id2) is not None) and (
                node_id1 is not node_id2):
            if node_id2 in self.outMap.get(node_id1) and node_id1 in self.inMap.get(node_id2):
                del self.outMap[node_id1][node_id2]
                del self.inMap[node_id2][node_id1]
                self.edgesSize = self.edgesSize - 1
                self.mc = self.mc + 1
                return True

        return False
