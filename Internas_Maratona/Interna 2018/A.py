
n = int(input())
soma = 0
lista = []

# os cinco primeiros numeros da sequencia são iguais
for i in range(5):
    lista.append(2)
    i = i + 1
    
#segunda parte da sequencia - soma dos ultimos 5 numeros
for j in range(n+1):
    soma = lista[j] + lista[j+1] + lista[j+2] + lista[j+3] + lista[j+4]
    lista.append(soma)
    soma = 0
    j = j + 1

# print (*lista)
print(lista[n])
