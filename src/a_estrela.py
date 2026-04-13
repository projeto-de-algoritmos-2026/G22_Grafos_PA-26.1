import heapq

def heuristica(a, b, coords):
    x1, y1 = coords[a]
    x2, y2 = coords[b]
    return abs(x1 - x2) + abs(y1 - y2)

def a_estrela(grafo, inicio, objetivo, coords):
    fila = []
    heapq.heappush(fila, (0, inicio))

    veio_de = {}
    custo = {inicio: 0}
    visitados = set()

    while fila:
        _, atual = heapq.heappop(fila)

        if atual in visitados:
            continue
        visitados.add(atual)

        if atual == objetivo:
            break

        for vizinho, base, tipo_peso, _ in grafo.adj[atual]:
            novo_custo = custo[atual] + tipo_peso

            if vizinho not in custo or novo_custo < custo[vizinho]:
                custo[vizinho] = novo_custo
                prioridade = novo_custo + heuristica(vizinho, objetivo, coords)
                heapq.heappush(fila, (prioridade, vizinho))
                veio_de[vizinho] = atual

    caminho = []
    atual = objetivo

    while atual != inicio:
        caminho.append(atual)
        atual = veio_de.get(atual)
        if atual is None:
            return [], float("inf")

    caminho.append(inicio)
    caminho.reverse()

    return caminho, custo[objetivo]