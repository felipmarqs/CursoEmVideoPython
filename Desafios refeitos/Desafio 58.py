import random
from time import sleep
cont = 1
n = random.randint(0,10) #Faz o computador "pensar"
a = int(input('Tente advinhar qual o número escolhido de 0 à 10:')) #O jogador tenta advinhar
while a != n:
    cont += 1
    if a > n:
        a = int(input('Menos, tente novamente: '))
    elif a < n:
        a = int(input('Mais, tente novamente:'))
print('Parabéns, você acertou em {} tentativa(s)'.format(cont))
