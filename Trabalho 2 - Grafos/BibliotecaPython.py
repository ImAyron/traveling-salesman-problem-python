import random




# extras

def abrirArquivo(NomeArq):
    arquivo = open(NomeArq, 'r')

    return arquivo


def fecharArquivo(Arq):
    Arq.close()


def converteEmListaSimples(G):
    aux = []
    for i in range(len(G)):
        aux2 = []
        for j in range(len(G[i])):
            aux2.append(int(G[i][j][0]))

        aux.append(aux2)

    return aux


# Representação

def converte_matriz1(arq):
    arq.seek(0)
    tamanhoArq = int(arq.readline().split()[0])
    matriz = [[0 for _ in range(tamanhoArq)] for _ in range(tamanhoArq)]

    linha = arq.readline()

    while linha != '':
        matriz[int(linha.split()[0])][int(linha.split()[1])] = float(linha.split()[2])
        matriz[int(linha.split()[1])][int(linha.split()[0])] = float(linha.split()[2])
        linha = arq.readline()

    return matriz


def converteLista(arq):
    arq.seek(0)
    linha1 = arq.readline()

    lista = [[] for i in range(int(linha1.split()[0]))]

    linha1 = arq.readline()
    while linha1 != '':
        el1 = linha1.split()[0]
        el2 = linha1.split()[1]
        el3 = linha1.split()[2]
        lista[int(el1)].append((int(el2), float(el3)))
        lista[int(el2)].append((int(el1), float(el3)))
        linha1 = arq.readline()

    return lista




# Trabalho 2 - Problema do caixeiro Viajante(PCV)
# Algoritmo Construtivo
def vizinhoMaisPróximo1(G):
    arestas = []
    listaux = []
    u = 0
    C = []
    Q = 0
    C.append(0)
    custo = 0
    while Q != len(G) - 1:
        menor = 3000000000
        vertice = 0
        for i in range(len(G[u])):
            if menor > G[u][i][1] and not C.__contains__(G[u][i][0]):
                menor = G[u][i][1]
                aux2 = i
                vertice = G[u][i][0]
                aux = vertice
        listaux.append(aux2)
        arestas.append((vertice, menor))
        Q = 1 + Q
        u = aux
        C.append(vertice)
        custo = custo + menor

    for i in range(len(G[aux])):
        if G[aux][i][0] == 0:
            arestas.append((0, G[aux][i][1]))
            listaux.append(i)
            custo = custo + G[aux][i][1]

    arquivo = open('saidaVizinhoMaisProximo.txt', 'w')
    arquivo.write(f'{custo}\n')

    for i in range(len(C)):
        arquivo.write(f'{C[i]}  '' ')
    arquivo.close()

    return C, arestas, listaux


def vizinhoMaisPróximo(G):
    arestas = []
    listaux = []
    u = 0
    C = []
    Q = 0
    C.append(0)
    custo = 0
    while Q != len(G) - 1:
        menor = 3000000000
        vertice = 0
        for i in range(len(G[u])):
            if menor > G[u][i][1] and not C.__contains__(G[u][i][0]):
                menor = G[u][i][1]
                aux2 = i
                vertice = G[u][i][0]
                aux = vertice
        listaux.append(aux2)
        arestas.append((vertice, menor))
        Q = 1 + Q
        u = aux
        C.append(vertice)
        custo = custo + menor

    for i in range(len(G[aux])):
        if G[aux][i][0] == 0:
            arestas.append((0, G[aux][i][1]))
            listaux.append(i)
            custo = custo + G[aux][i][1]
    # ler linha anterior
    arquivo = open('saidaVizinhoMaisProximo.txt', 'a+')
    arquivo.seek(0)
    custo_ant = arquivo.readline().split()[0]
    # print("Custo Anterior:"+custo_ant)
    arquivo.close()

    if float(custo_ant) > custo:
        arquivo = open('saidaVizinhoMaisProximo.txt', 'w')
        arquivo.write(f'{custo}\n')

        for i in range(len(C)):
            arquivo.write(f'{C[i]}  '' ')
        arquivo.close()

    # print("Custo atual:"+str(custo))

    return C, arestas, listaux


# Algoritmo de refinamento
def refinamento(G, optAux):
    aux2 = list(G)
    aux = list(G)
    print("\n")
    print('Caminho')
    print(optAux[0])
    print('Lista de Arestas')
    print(optAux[1])

    remove1 = random.randint(1, len(G) - 2)

    remove2 = random.randint(1, len(G) - 2)

    remove3 = random.randint(1, len(G) - 2)

    for i in range(len(G)):
        for j in range(len(G[i])):

            # 3-opt
            try:

                if i == optAux[0][remove1] and j == optAux[2][remove1]:
                    print('Remoção 1')
                    print(aux[i].pop(j))

                if i == optAux[0][remove2] and j == optAux[2][remove2]:
                    print('Remoção 2')
                    print(aux[i].pop(j))

                if i == optAux[0][remove3] and j == optAux[2][remove3]:
                    print('Remoção 3')
                    print(aux[i].pop(j))

            except:
                a = 0

    vizinhoMaisPróximo(aux2)
