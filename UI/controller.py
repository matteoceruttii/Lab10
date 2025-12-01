import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        if self._view.guadagno_medio_minimo.value.isdigit():
            self._view.lista_visualizzazione.clean()
            # prime informazioni da stampare
            self._view.lista_visualizzazione.controls.append(f"Numero di Hubs: {self._model.get_num_nodes()}")
            self._view.lista_visualizzazione.controls.append(f"Numero di Tratte: {self._model.get_num_edges(e)}")

            # informazioni sui vari archi e nodi
            for i in range(self._model.get_num_nodes()):
                self._view.lista_visualizzazione.controls.append(f"{i})"
                                                                 f"{self._model.costruisci_grafo(e)}")
        else:
            print('error')