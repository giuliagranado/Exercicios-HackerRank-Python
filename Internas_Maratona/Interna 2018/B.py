
# Entrada: 32 seleções
selecoes = []
for _ in range(32):
    nome, ranking = input().split()
    selecoes.append((nome, int(ranking)))

# Entrada: seleção alvo
alvo = input()

# Divide em grupos de 4 e ordena por ranking
grupos = []
for i in range(0, 32, 4):
    grupo = selecoes[i:i+4]
    grupo.sort(key=lambda x: x[1])  # menor ranking = melhor
    grupos.append(grupo)

# Mapeia posição da seleção
grupo_alvo = -1
for i in range(8):
    for j in range(4):
        if grupos[i][j][0] == alvo:
            grupo_alvo = i
            break
    if grupo_alvo != -1:
        break

# Define confrontos fixos das oitavas
confrontos = [
    (0, 1), (2, 3), (4, 5), (6, 7),
    (1, 0), (3, 2), (5, 4), (7, 6)
]

# Função para pegar 1º e 2º de um grupo
def get_classificados(g):
    return [grupos[g][0], grupos[g][1]]

# Função para simular caminho
def simular(alvo, melhor):
    caminho = []
    # Encontra o confronto de oitavas
    for idx, (g1, g2) in enumerate(confrontos):
        c1 = get_classificados(g1)
        c2 = get_classificados(g2)
        jogos = [(c1[0], c2[1]), (c2[0], c1[1])]
        for j in jogos:
            if alvo == j[0][0] or alvo == j[1][0]:
                atual = [j[0], j[1]]
                break
        else:
            continue
        break

    # Simula 4 fases
    for _ in range(4):
        # Remove a seleção atual
        outros = [s for s in atual if s[0] != alvo]
        if not outros:
            break
        # Escolhe adversário
        if melhor:
            escolhido = max(outros, key=lambda x: x[1])
        else:
            escolhido = min(outros, key=lambda x: x[1])
        caminho.append(escolhido[0])
        # Prepara próxima fase com o escolhido e um fictício
        atual = [(alvo, 0), escolhido]

    return caminho

# Simula melhor e pior caminho
melhor = simular(alvo, melhor=True)
pior = simular(alvo, melhor=False)

# Imprime
print(" ".join(melhor))
print(" ".join(pior))
