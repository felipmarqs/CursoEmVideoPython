n =int(input('Digite um número inteiro: '))
print('''Escolha uma base de conversão')
[ 1 ] para converter para BINÁRIO
[ 2 ] para converter para OCTAL
[ 3 ] para  converter para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido em BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('{} convertido em OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('{} convertido em HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida, tente novamente.')

