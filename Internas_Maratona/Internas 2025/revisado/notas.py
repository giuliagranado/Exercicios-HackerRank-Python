# Problema H - Notas do Professor  -  submetido e aceito

n = int(input())        #quantidade de monitores

todas_notas = [] 

for i in range(n):
    num_notas = int(input())          #quantidade de notas de cada monitor
    notas = input().split()           #recebe varias notas e armazena em uma lista
    for j in range(num_notas):
        todas_notas.append(notas[j])      #adiciona todas as notas em uma unica lista

ordenados = sorted(todas_notas, reverse=True)   #ordena em ordem decrescente
print(ordenados)