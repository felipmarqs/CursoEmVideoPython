print('{:=^40}'.format('Loja do seu José'))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual sua opção?'))
if opção == 1:
    desconto = preço - (preço *10/100)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preço,desconto))
elif opção ==2:
    desconto = preço - (preço *5/100)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preço,desconto))
elif opção ==3:
    parcela = preço / 2
    print('Sua compra vai custar R$ {:.2f}'.format(preço))
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20/100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final '.format(preço,total))
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totparc,parcela))
else:
    print('\033[0;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE\033[0;31m')