def ordenacao_topologica(grafo_dependencias):
    grau_entrada = {no: 0 for no in grafo_dependencias}

    for no in grafo_dependencias:
        for vizinho in grafo_dependencias[no]:
            grau_entrada[vizinho] += 1

    fila = [no for no in grau_entrada if grau_entrada[no] == 0]
    ordem = []

    while fila:
        atual = fila.pop(0)
        ordem.append(atual)

        for vizinho in grafo_dependencias[atual]:
            grau_entrada[vizinho] -= 1
            if grau_entrada[vizinho] == 0:
                fila.append(vizinho)

    if len(ordem) != len(grafo_dependencias):
        raise Exception("Erro: ciclo detectado!")

    return ordem