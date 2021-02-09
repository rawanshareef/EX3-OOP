from unittest import TestCase
from src.DiGraph import DiGraph


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

    return graph


class TestDiGraph(TestCase):

    def test_v_size(self):
        g = create_graph()
        self.assertEqual(5, g.v_size())

    def test_e_size(self):
        g = create_graph()
        self.assertEqual(6, g.e_size())

    def test_get_all_v(self):
        g = create_graph()
        keys = g.get_all_v().keys()
        i = 0
        for key in keys:
            self.assertEqual(key, i)
            i = i + 1

    def test_all_in_edges_of_node(self):
        g = create_graph()
        keys = g.all_in_edges_of_node(4).keys()
        answer = [1, 2]
        i = 0
        for key in keys:
            self.assertEqual(answer[i], key)
            i = i + 1

        values = g.all_in_edges_of_node(4).values()
        answer = [2, 0]
        j = 0
        for value in values:
            self.assertEqual(answer[j], value)
            j = j + 1

    def test_all_out_edges_of_node(self):
        g = create_graph()
        keys = g.all_out_edges_of_node(2).keys()
        answer = [3, 4]
        i = 0
        for key in keys:
            self.assertEqual(answer[i], key)
            i = i + 1

        values = g.all_out_edges_of_node(2).values()
        answer = [16, 0]
        j = 0
        for value in values:
            self.assertEqual(answer[j], value)
            j = j + 1

    def test_get_mc(self):
        g = create_graph()
        self.assertEqual(11, g.mc)
        g.remove_edge(1, 2)
        self.assertEqual(12, g.mc)

    def test_add_edge(self):
        g = create_graph()
        self.assertTrue(g.add_edge(2, 0, 5))
        self.assertFalse(g.add_edge(2, 4, 8))
        self.assertFalse(g.add_edge(2, 9, 3))
        self.assertFalse(g.add_edge(2, 2, 0))
        self.assertFalse(g.add_edge(1, 3, -2))

    def test_add_node(self):
        g = create_graph()
        self.assertTrue(g.add_node(5))
        self.assertFalse(g.add_node(5))

    def test_remove_node(self):
        g = create_graph()
        self.assertTrue(g.remove_node(4))
        self.assertFalse(g.remove_node(4))

    def test_remove_edge(self):
        g = create_graph()
        self.assertTrue(g.remove_edge(2, 4))
        self.assertFalse(g.remove_edge(4, 0))
        self.assertFalse(g.remove_edge(4, 5))
