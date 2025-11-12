# Problema F - Consultório Oftalmológico - resolvido no dia porém não submetido

string = input()
n = 0
for i in string:
    if ord(i) == ord("A"): # verifica se o caractere é "A"
        n += 1
print(n)