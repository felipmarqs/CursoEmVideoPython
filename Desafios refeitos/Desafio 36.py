'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.'''
print('\033[;36m-=-'*20)
print('\033[;31mSeja bem vindo à Lonlona Empréstimos!!!!')
print('\033[;36m-=-'*20)
nome = str(input('Qual seu nome?'))
vcasa = float(input('Nos informe por favor o valor da casa que deseja financiar: R$'))
salário = float(input('Informe para nós, o seu salário, por favor: R$'))
anos = int(input('Em quantos anos você pretende pagar a casa?'))
meses = anos * 12
prestação = vcasa / meses
c = salário * 30 / 100
print('Para pegar uma casa de R$ {} em {} anos a prestação será de R$ {:.2f}'.format(vcasa,anos,prestação))
if c < prestação:
    print('Desculpe {} , o empréstimo NEGADO.'.format(nome))
else:
    print('Tudo certo para o financiamento')