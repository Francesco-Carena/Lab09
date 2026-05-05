import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph=nx.Graph()
        self._nodes=None
        self._idMap = {}

    def buildGraph(self, miglia):
        self._graph.clear()
        self._nodes=None
        self._nodes=DAO.getAllNodes()
        for n in self._nodes:
            self._idMap[n.ID] = n

        self._graph.add_nodes_from(self._nodes)
        self.addEdges(miglia)


    def addEdges(self,miglia):
        connessioni=DAO.getEdges(miglia)
        for conn in connessioni:
            nodo_1 = self._idMap[conn.a1]
            nodo_2 = self._idMap[conn.a2]

            self._graph.add_edge(nodo_1, nodo_2, weight=conn.media_distanza)


    def get_numnodi(self):
        return len(self._graph.nodes())
    def get_numarchi(self):
        return len(self._graph.edges())
    def get_edges(self):
        return self._graph.edges(data=True)