import BibliotecaPython
import time

# Testes Biblioteca

#nomeDoArquivo = input("\n Digite o Nome do arquivo:")

#print("\nAbrindo o grafo do arquivo " + nomeDoArquivo)
arq = BibliotecaPython.abrirArquivo('a280.txt')
tempoDeExecução=20

execut=-1
while execut!=0:
        execut = int(input(
            "\nDigite 1 para  o vizinho mais próximo:"
            "\nDigite 0 para encerrar o programa:"))
        aux=0
        if int(execut) == 1:
            while aux<tempoDeExecução:

                # Code executed here

                BibliotecaPython.vizinhoMaisPróximo1(BibliotecaPython.converteLista(arq))
                #print('VIZINHO MAIS PRÓXIMO')
                #print('GRAFO FORMATO LISTA')
                #print(BibliotecaPython.converteLista(arq))
                #BibliotecaPython.vizinhoMaisPróximo(BibliotecaPython.converteLista(arq))
                BibliotecaPython.refinamento(BibliotecaPython.converteLista(arq),BibliotecaPython.vizinhoMaisPróximo(BibliotecaPython.converteLista(arq)))
                #print(BibliotecaPython.converteLista(arq))

                aux=aux+1
                # Code executed here
                time.sleep(1)


BibliotecaPython.fecharArquivo(arq)
#print("Fechando o grafo do arquivo " + nomeDoArquivo)
