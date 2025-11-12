# 23.10.25

# 1- Desafio: Você recebe três inteiros x, y e z representando 
# as dimensões de um cubo 3D. 
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result =  [[ i, j, k]
           
    for i in range (x + 1)
    for j in range(y + 1) 
    for k in range(z + 1) 
    if i + j + k != n ]
    
print(result)   


# 2 - desafio: Crie uma lista com todos os números de 0 a 20
# que sejam múltiplos de 3, mas não múltiplos de 5.

lista = [i for i in range(21) 
         if i % 3 == 0 and i % 5 != 0]

print(lista)

# 3 - testando range com start no negativo
# uma lista com todos os números negativos pares entre -10 e -1
pares = [i for i in range(-10, 0, 2)]
# uma lista com todos os números negativos ímpares entre -15 e -5
impares = [j for j in range(-15,-4, 2)]



# desafio 4 - Encontrar o segundo maior número em uma lista
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


print(sorted(set(arr))[-2])
