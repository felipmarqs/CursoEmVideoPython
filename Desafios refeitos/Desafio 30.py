#Crie um pograma que leia um número inteiro qualquer e mostre na tela se ele é par ou ímpar
número = int(input('DIGITE UM NÚMERO: '))
if número % 2 == 0:
    print('O número {} é PAR.'.format(número))
else:
    print('O número {} é IMPAR'.format(número))
