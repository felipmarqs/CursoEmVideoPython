import random
#Um professor quer sortear um dos seu quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido
aluno1 = str(input('Nome do 1ª aluno: '))
aluno2 = str(input('Nome do 2º aluno: '))
aluno3 = str(input('Nome do 3º aluno: '))
aluno4 = str(input('Nome do 4º aluno: '))
lista = aluno1, aluno2, aluno3, aluno4
escolhido = random.choice(lista)
print(f'O aluno escolhido foi o {escolhido}. ')
