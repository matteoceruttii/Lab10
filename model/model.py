import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()


# funzione che restituisce il grafo inserendo tutti gli hub presenti e filtrando le tratte tramite guadagno medio
    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # aggiungo i nodi
        self._nodes = self.G.add_nodes_from(DAO.load_hub())

        # aggiungo gli archi
        self._edges = self.G.add_edges_from(DAO.load_archi_spedizioni())


# funzione che restituisce il numero di tratte del grafo
    def get_num_edges(self, val):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        return self.G.number_of_edges()


# funzione che restituisce il numero totalte di nodi
    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        return self.G.number_of_nodes()


# funzione che restituisce tutte le tratte, anche quelle non soggette a selezione dall'utente
    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        return self.G.edges()