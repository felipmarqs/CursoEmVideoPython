maisbarato = total = produtosmaismil = cont = 0
produtobarato = ''
print('-' *20)
print(str('Lojas super baratão'))
print('-'*20)
while True:
    cont += 1
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    if preço >= 1000:
        produtosmaismil += 1
    if  cont == 1:
        produtobarato = produto
        maisbarato = preço
    if produto < produtobarato:
        produtobarato = produto
        maisbarato = preço
    total += preço
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
    while continuar not in 'S':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {produtosmaismil:.2f} produtos custando mais de R$1000')
print(f'O produto mais barato foi {produtobarato} que custa R${maisbarato:.2f}')