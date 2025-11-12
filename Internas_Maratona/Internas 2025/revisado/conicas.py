# Problema B - Cônicas  -  submetido e aceito

reais = input().split(",")

# coeficientes da equação geral da cônica
A = float(reais[0])
B = float(reais[1])
C = float(reais[2])
D = float(reais[3])
E = float(reais[4])
F = float(reais[5])

# matriz dos coeficientes
d = [[A,(B/2),(D/2)],[(B/2),C,(E/2)],[(D/2),(E/2),F]]
d11 = [[C,(E/2)],[(E/2),F]]
d33 = [[A,(B/2)],[(B/2),C]]
d22 = [[A,(D/2)],[(D/2),F]]

t = A+C

# calculo do determinante da matriz 3x3
detd = (d[0][0]*d[1][1]*d[2][2])+(d[0][1]*d[1][2]*d[2][0])+(d[0][2]*d[1][0]*d[2][1])-(d[0][1]*d[1][0]*d[2][2])-(d[0][0]*d[1][2]*d[2][1])-(d[0][2]*d[1][1]*d[2][0])

# função para calcular o determinante de uma matriz 2x2
def detquadrada(matriz):
    det = (matriz[0][0]*matriz[1][1])-(matriz[0][1]*matriz[1][0])
    return det

detd11 = detquadrada(d11)
detd22 = detquadrada(d22)
detd33 = detquadrada(d33)

# classificação da cônica
if detd33>0:
    if detd == 0:
        print("Um ponto")
    else:
        if t*detd > 0:
            print("Conjunto vazio")
        else:
            if A==C and B==0:
                print("Circunferencia")
            else:
                print("Elipse")
if detd33<0:
    if detd == 0:
        print("Duas retas concorrentes")
    else:
        print("Hiperbole")
    
if detd33==0:
    if detd == 0:
        if (detd11+detd22)>0:
            print("Conjunto vazio")
        else:
            print("Duas retas paralelas")
    else:

        print("Parabola")
