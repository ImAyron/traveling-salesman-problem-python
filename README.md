# Biblioteca de Grafos e Problema do Caixeiro Viajante

> Biblioteca de grafos em Python com buscas em largura/profundidade e heurística do vizinho mais próximo para o TSP, testada em instâncias da TSPLIB.
> A Python graph library with breadth/depth-first search and a nearest-neighbor heuristic for the TSP, benchmarked on TSPLIB instances.

---

## 🇧🇷 Português

### Sobre

Trabalho da disciplina de **Grafos**. Implementa uma biblioteca de grafos em Python do zero e a aplica ao **Problema do Caixeiro Viajante** (TSP), usando a heurística construtiva do **vizinho mais próximo**.

### Algoritmos

- **Busca em largura (BFS)** — saída em `buscaLarguraResult.txt`
- **Busca em profundidade (DFS)** — saída em `buscaProfundidadeResult.txt`
- **Vizinho mais próximo (TSP)** — saída em `saidaVizinhoMaisProximo.txt`

### Instâncias de teste

Instâncias clássicas da **TSPLIB**, nomeadas pelo número de cidades:

| Arquivo | Cidades |
|---|---|
| `ch130.txt` | 130 |
| `a280.txt` | 280 |
| `ali535.txt` | 535 |
| `gr666.txt` | 666 |
| `fl1577.txt` | 1577 |

### Arquivos

```
BibliotecaPython.py   Implementação da biblioteca de grafos e dos algoritmos
chamadaFunc.py        Script de execução: carrega a instância e chama os algoritmos
*.txt                 Instâncias de entrada e arquivos de resultado
```

### Como executar

```bash
cd "Trabalho 2 - Grafos"
python chamadaFunc.py
```

Edite `chamadaFunc.py` para escolher qual instância carregar e quais algoritmos executar. Os resultados são gravados nos arquivos `.txt` correspondentes.

---

## 🇺🇸 English

### About

Coursework for a **Graph Theory** class. Implements a graph library in Python from scratch and applies it to the **Traveling Salesman Problem** (TSP) using the **nearest-neighbor** constructive heuristic.

### Algorithms

- **Breadth-first search (BFS)** — output in `buscaLarguraResult.txt`
- **Depth-first search (DFS)** — output in `buscaProfundidadeResult.txt`
- **Nearest neighbor (TSP)** — output in `saidaVizinhoMaisProximo.txt`

### Benchmark instances

Classic **TSPLIB** instances, named after their city count:

| File | Cities |
|---|---|
| `ch130.txt` | 130 |
| `a280.txt` | 280 |
| `ali535.txt` | 535 |
| `gr666.txt` | 666 |
| `fl1577.txt` | 1577 |

### Files

```
BibliotecaPython.py   Graph library and algorithm implementations
chamadaFunc.py        Driver script: loads an instance and runs the algorithms
*.txt                 Input instances and result files
```

### Running

```bash
cd "Trabalho 2 - Grafos"
python chamadaFunc.py
```

Edit `chamadaFunc.py` to pick which instance to load and which algorithms to run. Results are written to the matching `.txt` files.
