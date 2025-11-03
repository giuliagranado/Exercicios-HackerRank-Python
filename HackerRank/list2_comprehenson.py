#27.10.25

# exercicio 1 - Encontrar o segundo menor número em uma lista
if __name__ == '__main__':
     
    students = []      #lista principal fora do loop

    for x in range(int(input())):   # quantos alunos e notas serão
        name = input()
        score = float(input())
        students.append([name, score])  # junta nome e nota numa lista
    
    # extrai as notas, remove as duplicadas e ordena
    scores = sorted(set([s[1] for s in students]))    
    second_lowest = scores[1]
    
    # filtra os nomes com a menor nota
    names = [t[0] for t in students if t[1] == second_lowest]
    for name in sorted(names, key =str.lower) :
        print(name)


# exercicio 2 - receber nomes e notas, calcular a média final
if __name__ == '__main__':
    
    n = int(input())
    student_marks = {}
    
    for x in range(n):
        name, *line = input().split() 
        scores = list(map(float, line)) # converte para float
        student_marks[name] = scores
    query_name = input()
    
    notas = student_marks[query_name]
    media = sum(notas)/len(notas)   # calcular a média
    
    # exibir a média com 2 casas decimais
    print (f"{media:.2f}")     
    
