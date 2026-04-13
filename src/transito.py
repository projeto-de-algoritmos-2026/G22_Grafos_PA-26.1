def aplicar_transito(grafo, horario):
    for u in grafo.adj:
        novas = []
        for v, base, tipo_peso, _, tipo in grafo.adj[u]:

            fator = 1

            if 7 <= horario <= 9:
                fator = 1.8
            elif 18 <= horario <= 20:
                fator = 2.0
            elif 12 <= horario <= 14:
                fator = 1.3

            peso_dinamico = tipo_peso * fator

            novas.append((v, base, tipo_peso, peso_dinamico, tipo))

        grafo.adj[u] = novas