#27.10.25

#exercicio 1 - Encontrar o número de alunos que estão em ambos
if __name__ == '__main__':
    news_french = int(input())
    matriculas_french = input().split()
    news_english = int(input())
    matriculas_english = input().split()

    # juntando as duas listas
    alunos = matriculas_english + matriculas_french 
    
    visto = set()
    duplicata = set()
    
    for aluno in alunos:
        if aluno in visto:
            duplicata.add(aluno)
        else:
            visto.add(aluno)
        
    quantidade = len(duplicata)        
    print (quantidade)


# usando o set intersection
if __name__ == '__main__':
    n_english = int(input())
    english = set(input().split())

    n_french = int(input())
    french = set(input().split())

    ambos = english & french
    #ambos = english.intersection(french) -> mesma coisa
    print(len(ambos))
