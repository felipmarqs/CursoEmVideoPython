n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
opção = 0
while opção != 5:
    print('''   [1]somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opção = int(input('>>>>>>>>>Qual a sua opção??? '))
    if opção == 1:
        s = n1 + n2
        print('A soma de {} e {} é {}'.format(n1,n2,s))
    elif opção == 2:
        m = n1 * n2
        print('O resultado de {} vezes {} é {}'.format(n1,n2,m))
    elif opção == 3:
        if n1 > n2:
           maior = n1
        else:
           maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1,n2,maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor:'))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente')
