# Problema A - Computador Intcode  - não submetido

seq = list(map(int, input().split(",")))  # converte tudo para int

for i in range(0, len(seq), 4):
    if seq[i] == 1:  # soma
        pos = seq[i+3]
        sum1 = seq[i+1]
        sum2 = seq[i+2]
        seq[pos] = seq[sum1] + seq[sum2]

    elif seq[i] == 2:  # multiplicação
        pos = seq[i+3]
        sum1 = seq[i+1]
        sum2 = seq[i+2]
        seq[pos] = seq[sum1] * seq[sum2]

    elif seq[i] == 99:  # finaliza o programa
        break

    else:
        num = -1
        break

num = seq[0]
print(num)
