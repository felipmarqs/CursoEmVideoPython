#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
import time
computador = random.randint(1,5)
print('Pensei um número! ')
jogador = int(input('Tente adivinhar o número que eu pensei (1 á 5): '))
if jogador == computador:
    print('Parabéns você acertou!')
else:
    print('Você errou!')
print(f'O número que eu pensei foi {computador}')