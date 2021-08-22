import BibliotecaPython
import time

# Testes Biblioteca

nomeDoArquivo = input("\n Digite o Nome do arquivo:")

print("\nAbrindo o grafo do arquivo " + nomeDoArquivo)
arq = BibliotecaPython.abrirArquivo(nomeDoArquivo)
tempoDeExecução = time.time() + float(input("\nDigite o tempo de execução:"))+5
BibliotecaPython.vizinhoMaisPróximo1(BibliotecaPython.converteLista(arq))


while time.time() < tempoDeExecução:


    BibliotecaPython.refinamento(BibliotecaPython.converteLista(arq),
                                 BibliotecaPython.vizinhoMaisPróximo(BibliotecaPython.converteLista(arq)))



BibliotecaPython.fecharArquivo(arq)
# print("Fechando o grafo do arquivo " + nomeDoArquivo)
