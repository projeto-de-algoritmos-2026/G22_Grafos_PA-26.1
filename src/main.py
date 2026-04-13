from grafo import Grafo
from a_estrela import a_estrela
from visualizacao import plotar
from topologica import ordenacao_topologica


def construir_grafo():
    grafo = Grafo()

    grafo.adicionar_aresta("Hotel", "Museu", 2, "avenida")
    grafo.adicionar_aresta("Hotel", "Parque", 4, "rua")
    grafo.adicionar_aresta("Museu", "Restaurante", 3, "rua")
    grafo.adicionar_aresta("Parque", "Restaurante", 2, "avenida")
    grafo.adicionar_aresta("Restaurante", "Show", 5, "rodovia")

    coords = {
        "Hotel": (0, 0),
        "Museu": (2, 2),
        "Parque": (1, 4),
        "Restaurante": (4, 3),
        "Show": (6, 1)
    }

    return grafo, coords


def executar():
    grafo, coords = construir_grafo()


  
    dependencias = {
        "Hotel": ["Museu"],
        "Museu": ["Restaurante"],
        "Restaurante": ["Show"],
        "Show": []
    }


    try:
        ordem = ordenacao_topologica(dependencias)
        print("\nOrdem topológica:", " → ".join(ordem))
    except Exception as e:
        print("\n", e)
        return

  
    print("\n📍 Pontos disponíveis:")
    for ponto in coords:
        print("-", ponto)

    inicio_input = input("\nDigite o ponto de INÍCIO: ").strip().lower()
    destino_input = input("Digite o ponto de DESTINO: ").strip().lower()

    mapa = {p.lower(): p for p in coords}

    if inicio_input not in mapa or destino_input not in mapa:
        print("Ponto inválido!")
        print("Use:", ", ".join(coords.keys()))
        return

    inicio = mapa[inicio_input]
    destino = mapa[destino_input]

    
    if inicio not in ordem or destino not in ordem:
        print("Pontos não estão nas dependências!")
        return

    if ordem.index(inicio) > ordem.index(destino):
        print("Ordem inválida! Viola dependências.")
        return

    
    caminho, custo = a_estrela(grafo, inicio, destino, coords)

    if not caminho:
        print("Não foi possível encontrar rota!")
        return

    print("\n Melhor rota encontrada:")
    print(" → ".join(caminho))
    print("Custo:", round(custo, 2))

    
    plotar(grafo, coords, caminho, inicio, destino)


if __name__ == "__main__":
    executar()