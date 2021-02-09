import copy
import heapq
import json
import math
from typing import List
import matplotlib.pyplot as plt
import numpy as py
import random

from src.DiGraph import DiGraph, NodeData
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface


class NodeAlgo:
    """ this class represents a node in a directional weighted graph, and presents his father.
    This class was created in order we can save the father in Dijkstra algorithm."""

    def __init__(self, key: int = None, info="", weight: float = None, father: NodeData = None):
        """method is similar to constructor in java. this method used to initialize the node state."""
        self.key = key
        self.info = info
        self.weight = weight
        self.father = father

    def __lt__(self, x):
        """compare between two NodeAlgo by their weight"""
        return self.weight < x.weight

    def __repr__(self):
        """ function returns a printable representation of the node.
        @return: node string"""
        return f'NodeAlgo: {self.key} , info= {self.info}, weight= {self.weight}, father= {self.father}'


class GraphAlgo(GraphAlgoInterface):
    """ This class do algorithmic operations on an directional weighted graph that created by "DiGraph"."""
    def __init__(self, graph: DiGraph = None):
        """method is similar to constructor in java. this method used to initialize the graph state."""
        self.graph = graph

    def init(self, graph):
        """method is similar to constructor in java. this method used to initialize the graph state."""
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        """ return the directed graph on which the algorithm works on.
        @return: graph"""
        return self.graph

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """ check the shortest path from node id1 to node id2 using Dijkstra's Algorithm.
        this method save the father to each node and in this way save a path of nodes between id1 and id2.
        also, this method update the weight to each node in order to find the minimal distance.
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        if there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])"""

        if self.graph is None:
            return math.inf, []

        graph_nodes = self.graph.get_all_v()

        if (graph_nodes.get(id1) is None) or (graph_nodes.get(id2) is None):
            return math.inf, []

        if id1 == id2:
            return 0, [id1]

        # Dijkstra method
        parent_map = {}
        start = NodeAlgo(key=id1, info="not visited", weight=0)
        q = [start]
        parent_map[id1] = start

        for node in graph_nodes:
            if node != id1:
                new_node = NodeAlgo(key=node, info="not visited", weight=math.inf)
                parent_map[node] = new_node

        while q:
            temp = q[0]
            for n, w in self.graph.all_out_edges_of_node(temp.key).items():
                if parent_map[n].info == "not visited":
                    path = temp.weight + w
                    node_weight = parent_map[n].weight
                    if path < node_weight:
                        parent_map[n].weight = path
                        parent_map[n].father = graph_nodes.get(temp.key)
                        heapq.heappush(q, parent_map[n])
            temp.info = "visited"
            heapq.heappop(q)

        # find dist and list
        if parent_map[id2].info == "not visited":
            return math.inf, []
        else:
            dist = parent_map[id2].weight
            current = parent_map[id2]
            list1 = []
            while current.key != id1:
                list1.append(graph_nodes[current.key])
                current = parent_map[current.father.key]
            list1.append(graph_nodes[id1])
            list2 = []
            while list1:
                p = list1.pop()
                list2.append(p.key)

            return dist, list2

    def bfs(self, src: int, flag: bool) -> (float, list):
        """ this class is a help function to "connected_component".
            this method get src key, and bool.
            if the bool is True- the method check which of the nodes src can get(from the nodes that get out of him).
            if the bool is False-  the method check which nodes get in of src.
            bfs algorithm uses a queue in order to store the nodes and go over the graph.
            The algorithm changes the nodes tags from 0 to 1, and in this way build the list.
            * @param src, bool
            * @return list"""
        graph_nodes = self.graph.get_all_v()
        # zeroing all tags
        for node in graph_nodes:
            graph_nodes[node].tag = 0

        new_list = []
        q = []
        temp = graph_nodes[src]
        q.append(temp)
        new_list.append(temp.key)
        graph_nodes[temp.key].tag = 1
        while q:
            temp = q.pop()
            if flag:
                for n in self.graph.all_out_edges_of_node(temp.key).keys():
                    if graph_nodes[n].tag == 0:
                        q.append(graph_nodes[n])
                        graph_nodes[n].tag = 1
                        new_list.append(graph_nodes[n].key)
            else:
                for n in self.graph.all_in_edges_of_node(temp.key).keys():
                    if graph_nodes[n].tag == 0:
                        q.append(graph_nodes[n])
                        graph_nodes[n].tag = 1
                        new_list.append(graph_nodes[n].key)

        return new_list

    def connected_component(self, id1: int) -> list:
        """ finds the Strongly Connected Component(SCC) that node id1 is a part of.
        This method based on BFS Algorithm.
        the method get a node id and find his SCC.
        in order to do this, we check which nodes id1 can arrive,
        and after this, we check the nodes that can arrive to id1.
        Finally, we compare between the 2 lists and We return the common nodes.
        @param id1: The node id
        @return: The list of nodes in the SCC
        if the graph is None or id1 is not in the graph, the function should return an empty list []"""
        if self.graph is None:
            return []

        graph_nodes = self.graph.get_all_v()
        if id1 not in graph_nodes:
            return []

        answer_list = []
        straight_tracking = self.bfs(id1, True)
        back_tracking = self.bfs(id1, False)

        for s in straight_tracking:
            for b in back_tracking:
                if s == b and s not in answer_list:
                    answer_list.append(s)
                    break

        return answer_list

    def connected_components(self) -> List[list]:
        """ finds all the Strongly Connected Component(SCC) in the graph.
            this method pass all the nodes in the graph and find the SCC for each node.
            this method use connected_component.
            @return: The list all SCC
            if the graph is None the function should return an empty list []
            """
        if self.graph is None:
            return []
        big_list = []
        done = []
        graph_nodes = self.graph.get_all_v()
        for n in graph_nodes:
            if n not in done:
                mini_list = self.connected_component(n)
                if mini_list:
                    big_list.append(mini_list)
                    done = done + mini_list
        return big_list

    def load_from_json(self, file_name: str) -> bool:
        """ loads a graph from a json file.
            @param file_name: The path to the json file
            @returns True if the loading was successful, False o.w."""

        if file_name is None:
            return False

        try:
            with open(file_name) as f:
                load_graph = json.load(f)
            self.graph = DiGraph()
            nodes = load_graph["Nodes"]
            edges = load_graph["Edges"]
            for n in nodes:
                if n.get('pos') is not None:
                    self.graph.add_node(n.get('id'), tuple(map(float, n.get("pos").split(","))))
                else:
                    self.graph.add_node(n.get('id'))
            for e in edges:
                self.graph.add_edge(e.get('src'), e.get('dest'), e.get('w'))
            return True
        except IOError:
            return False

    def save_to_json(self, file_name: str) -> bool:
        """ saves the graph in JSON format to a file
            @param file_name: The path to the out file
            @return: True if the save was successful, False o.w."""
        edges = []
        nodes = []

        if self.graph is None or file_name is None:
            return False

        graph_nodes = self.graph.get_all_v()
        for k in graph_nodes.keys():
            if graph_nodes[k].pos is not None:
                nodes.append({"id": graph_nodes[k].key, "pos": graph_nodes[k].pos})
            else:
                nodes.append({"id": graph_nodes[k].key})

        for src in graph_nodes:
            for dest, w in self.graph.all_out_edges_of_node(src).items():
                edges.append({"src": src, "w": w, "dest": dest})

        save_graph = {"Edges": edges, "Nodes": nodes}

        try:
            with open(file_name, "w") as json_graph:
                json.dump(save_graph, json_graph)
        except IOError:
            return False

        return True

    def plot_graph(self) -> None:
        """ plots the graph.
            if the nodes have a position, the nodes will be placed there.
            Otherwise, they will be placed in a random but elegant manner.
            @return: None """
        graph_nodes = self.graph.get_all_v()
        for n in graph_nodes.keys():
            if graph_nodes[n].pos is None:
                x = random.uniform(0.0, 10000)
                y = random.uniform(0.0, 10000)
                graph_nodes[n].pos = (x, y, 0.0)
            plt.plot(graph_nodes[n].pos[0], graph_nodes[n].pos[1], ".", markersize=10, color="blue")
            plt.text(graph_nodes[n].pos[0], graph_nodes[n].pos[1], str(n), color="red", fontsize=10)

        for src in graph_nodes.keys():
            for dest in self.graph.all_out_edges_of_node(src).keys():
                plt.annotate("", xy=(graph_nodes[src].pos[0], graph_nodes[src].pos[1]),
                             xytext=(graph_nodes[dest].pos[0], graph_nodes[dest].pos[1]),
                             arrowprops=dict(arrowstyle="<-"))
        plt.show()
