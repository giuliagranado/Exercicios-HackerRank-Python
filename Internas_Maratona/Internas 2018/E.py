
n = int(input())
string = list(input())

peso = 0
valido = True

for caractere in string:
    if caractere == "(":
        peso += 1
    elif caractere == ")":
        peso -= 1
    if peso < 0:  #verifica se o parenteses fecha antes de abrir
        print("falso")
        valido = False
        break

#se ja foi marcado como falso, nao precisa verificar mais
if not valido or peso != 0: 
        print("falso")
elif peso == 0:
        print("verdadeiro")