class Grafo:
    def __init__(self):
        self.adj = {}

    def adicionar_aresta(self, u, v, peso, tipo_via="rua"):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []

        fator_tipo = {
            "rua": 1,
            "avenida": 0.8,
            "rodovia": 0.6
        }

        peso_tipo = peso * fator_tipo.get(tipo_via, 1)

        # (destino, base, final, tipo)
        self.adj[u].append((v, peso, peso_tipo, tipo_via))
        self.adj[v].append((u, peso, peso_tipo, tipo_via))