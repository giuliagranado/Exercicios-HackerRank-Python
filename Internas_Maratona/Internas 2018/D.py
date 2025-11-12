
# Entrada 1: número de moedas
n = int(input())

# Entrada 2: todas as moedas e taxas em uma única linha
entrada_moedas = input().split()

# Entrada 3: valor em HKD
valor = float(input())

# Separar siglas e taxas
siglas = []
taxas = []

for i in range(0, len(entrada_moedas), 2):
    siglas.append(entrada_moedas[i])
    taxas.append(float(entrada_moedas[i + 1]))

# Calcular e imprimir a quantidade de cada moeda
for i in range(n):
    quantidade = (100 * valor) / taxas[i]
    print(f"{siglas[i]} {quantidade:.2f}")
