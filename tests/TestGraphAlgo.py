from math import inf
from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


def create_graph() -> DiGraph:
    graph = DiGraph()
    for i in range(5):
        graph.add_node(i)

    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 3, 4)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 4, 2)
    graph.add_edge(2, 3, 16)
    graph.add_edge(2, 4, 0)
    graph.add_edge(4, 1, 2.5)
    graph.add_edge(4, 0, 7.2)
    return graph


class TestGraphAlgo(TestCase):
    def test_shortest_path(self):
        g1 = create_graph()
        g2 = GraphAlgo()
        g2.init(g1)
        self.assertEqual((1, [1, 2, 4]), g2.shortest_path(1, 4))
        self.assertEqual((12.2, [1, 2, 4, 0, 3]), g2.shortest_path(1, 3))
        self.assertEqual((3, [0, 1, 2, 4]), g2.shortest_path(0, 4))
        self.assertEqual((1, [1, 2, 4]), g2.shortest_path(1, 4))
        self.assertEqual((0, [1]), g2.shortest_path(1, 1))
        self.assertEqual((inf, []), g2.shortest_path(9, 1))

        g3 = DiGraph()
        g4 = GraphAlgo()
        g4.init(g3)
        self.assertEqual((inf, []), g4.shortest_path(0, 1))

        g1.add_node(5)
        g1.add_node(6)
        g1.add_edge(4, 5, 3)
        g1.add_edge(5, 6, 4)
        g2.init(g1)
        self.assertEqual((8, [1, 2, 4, 5, 6]), g2.shortest_path(1, 6))

    def test_connected_component(self):
        g1 = create_graph()
        g2 = GraphAlgo()
        g2.init(g1)
        self.assertEqual([1, 2, 4, 0], g2.connected_component(1))
        g1.remove_edge(4, 0)
        g2.init(g1)
        self.assertEqual([1, 2, 4], g2.connected_component(1))

    def test_connected_components(self):
        g1 = create_graph()
        g2 = GraphAlgo()
        g1.remove_edge(4, 0)
        g1.add_node(5)
        g1.add_node(6)
        g1.add_node(7)
        g1.add_node(8)
        g1.add_edge(3, 7, 2)
        g1.add_edge(4, 6, 4)
        g1.add_edge(6, 8, 2)
        g1.add_edge(8, 5, 1)
        g1.add_edge(7, 3, 3)
        g1.add_edge(5, 6, 9)
        g2.init(g1)
        self.assertEqual([[0], [1, 2, 4], [3, 7], [5, 6, 8]], g2.connected_components())

    def test_save_load_from_json(self):
        ga = GraphAlgo()
        self.assertTrue(ga.load_from_json("../data/G_10_80_1.json"))
        self.assertTrue(ga.save_to_json("my_Json"))

    def test_plot_graph(self):
        # pos is not None
        g1 = GraphAlgo()
        self.assertTrue(g1.load_from_json("../data/A5"))
        self.assertTrue(g1.save_to_json("my_Json"))
        g1.plot_graph()

        # pos is None
        g2 = GraphAlgo()
        self.assertTrue(g2.load_from_json("../data/G_10_80_1.json"))
        self.assertTrue(g2.save_to_json("my_Json"))
        g2.plot_graph()
