import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


def plotar(grafo, coords, caminho=None, inicio=None, destino=None):
    plt.figure()

    cores_via = {
        "rua": "gray",
        "avenida": "blue",
        "rodovia": "green"
    }

    desenhadas = set()


    # RUAS
    for u in grafo.adj:
        for v, base, tipo_peso, tipo in grafo.adj[u]:

            if (v, u) in desenhadas:
                continue
            desenhadas.add((u, v))

            x = [coords[u][0], coords[v][0]]
            y = [coords[u][1], coords[v][1]]

            cor = cores_via.get(tipo, "black")

            plt.plot(x, y, linestyle='--', linewidth=1.5, color=cor, zorder=1)

            xm = (coords[u][0] + coords[v][0]) / 2
            ym = (coords[u][1] + coords[v][1]) / 2

            texto = f"{tipo}\nbase:{base}\nfinal:{round(tipo_peso,1)}"
            plt.text(xm, ym, texto, fontsize=8)

    # ROTA
    if caminho:
        for i in range(len(caminho) - 1):
            u = caminho[i]
            v = caminho[i + 1]

            x = [coords[u][0], coords[v][0]]
            y = [coords[u][1], coords[v][1]]

            plt.plot(x, y, linewidth=3, color='red', marker='o', zorder=3)

    # PONTOS DINÂMICOS
    for no, (x, y) in coords.items():

        if no == inicio:
            plt.scatter(x, y, s=140, marker='s', color='green', zorder=4)

        elif no == destino:
            plt.scatter(x, y, s=160, marker='*', color='blue', zorder=4)

        else:
            plt.scatter(x, y, s=80, color='black', zorder=4)

        plt.text(x + 0.1, y + 0.1, no)

    # LEGENDA
    legend_elements = [
        Line2D([0], [0], color='blue', linestyle='--', label='Avenida'),
        Line2D([0], [0], color='gray', linestyle='--', label='Rua'),
        Line2D([0], [0], color='green', linestyle='--', label='Rodovia'),
        Line2D([0], [0], color='red', linewidth=3, marker='o', label='Rota ótima'),
        Line2D([0], [0], marker='s', color='green', linestyle='None', label='Início'),
        Line2D([0], [0], marker='*', color='blue', linestyle='None', label='Destino')
    ]

    plt.legend(handles=legend_elements)

    plt.title("A* com Tipos de Via (Entrada Dinâmica)")
    plt.grid(True)

    plt.savefig("rota.png")
    print("Imagem salva como rota.png")