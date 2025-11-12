# Problema G - Serpente Dourada  -  submetido e aceito

q = int(input())
anos = input().split()
n = 0

# contagem dos anos que são simultaneamente do serpente(12) e são considerados anos dourados(7)
for i in anos:
    if (int(i)+3)%12 == 0:
        if (int(i)-2)%7 == 0:
            n+=1
print(n)
