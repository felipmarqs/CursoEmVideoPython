resp = 'S'
quant = média = soma = maior = menor = 0
while resp in 'sS':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar ? [S/N]')).upper().strip()[0]
média = soma / quant
print(f'Você digitou {quant} números e a média foi {média}')
print('O maior valor foi {} e o menor número foi {}'.format(maior,menor))