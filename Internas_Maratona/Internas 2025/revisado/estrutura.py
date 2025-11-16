# Problema E - Adivinhe a estrutura  -  não submetido

# erro principal: tratar a entrada como string, mas comparar como se fosse números

n = int(input())

linhas = []
for i in range(n):
    operacoes = list(map(int, input().split()))  # converte para int
    linhas.append(operacoes)
 
def pilhas(linhas):
    pilha = []
    pilha_pos = True
    for i in linhas:
        if i[0] == 1: # inserir
            pilha.append(i[1])
        elif i[0] == 2: # deletar
            if not pilha or i[1] != pilha[-1]:
                pilha_pos = False
                break
            pilha.pop()
    return pilha_pos
                
def fila(linhas):
    fila = []
    fila_pos = True
    for i in linhas:
        if i[0] == 1: # inserir
            fila.append(i[1])
        elif i[0] == 2: # deletar
            if not fila or i[1] != fila[0]:
                fila_pos = False
                break
            del(fila[0])
    return fila_pos

def prio(linhas):
    prio = []
    prio_pos = True
    for i in linhas:
        if i[0] == 1: # inserir
            prio.append(i[1])
        elif i[0] == 2: # deletar
            if not prio or i[1] != max(prio):
                prio_pos = False
                break
            prio.remove(max(prio))
    return prio_pos
    

resultado = [pilhas(linhas), fila(linhas), prio(linhas)] 

print(resultado)
  
if resultado[0]==resultado[1]==resultado[2]==False:
    print("nenhum")
elif resultado[0]==True and resultado[1]==resultado[2]==False:
    print("pilha")
elif resultado[1]==True and resultado[0]==resultado[2]==False:
    print("fila")
elif resultado[2]==True and resultado[1]==resultado[0]==False:
    print("fila de prioridade")
else:
    print("inconclusivo")
