import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analisi(self, e):
        self._view.txt_result.clean()
        inp=self._view.txt_airportid.value
        if not inp:
            self._view.create_alert("Inserisci una distanza minima!")
            return
        try:
            miglia=int(inp)
        except ValueError:
            self._view.txt_result.controls.clean()
            self._view.txt_result.controls.append(ft.Text("Attenzione inserire un valore numerico", color="red"))
            self._view.update_page()
            return

        self._model.buildGraph(miglia)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo è costituito da {self._model.get_numnodi()} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo è costituito da {self._model.get_numarchi()} archi"))
        edges=self._model.get_edges()
        for edge in edges:
            self._view.txt_result.controls.append(
                ft.Text(f"{edge[0]} <---> {edge[1]} | Distanza media: {edge[2]["weight"]:.2f} miglia"))

        self._view.update_page()
