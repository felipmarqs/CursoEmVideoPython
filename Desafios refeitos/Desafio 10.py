#Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Opicional Euros e Libras
R=float(input('Quantos reais você tem na carteira?'))
print('Então você pode comprar :')
D= R*0.278225
E= R*0.23477318
L= R*0.205329982
print('{:.2f} dólares'.format(D))
print('{:.2f} euros'.format(E))
print('{:.2f} libras'.format(L))
