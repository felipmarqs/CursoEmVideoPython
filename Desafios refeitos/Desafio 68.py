from random import randint
v = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(1,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}.Total de {total}',end = ' ')
    print('DEU PAR'if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            v += 1
        else:
            print('Game over!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Ganhou')
            v+=1
        else:
            print('GAME OVER!')
            break
    print('Vamos jogar novamente...')
print(f'Você ganhou {v} vezes.')
