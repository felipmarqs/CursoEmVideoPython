n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
m = (n1 + n2) /2
print('A média do aluno é {}'.format(m))
if m < 5:
    print('O aluno está REPROVADO!')
elif m >= 5 and m < 6.9:
    print('O aluno está em RECUPERAÇÃO!!')
elif m >= 7:
    print('O aluno está APROVADO')