#Faça um programa que leia a largura de uma parede em metros,calcule sua área e
# a quantidade de tinta necessária para pintá-la,sabendo que cada litro de tinta pinta uma área de 2m²
print('Vamos calcular quanta tinta precisamos para pintar essa parede! ')
al = float(input('Qual a altura dessa parede em metros?'))
la = float(input('Qual a largura dessa parede?'))
área = al*la
litros = área/2
print(f'Será necessário {litros:.2f} litros de tinta para pintar a parede de {área:.2f} m²')
fim = 'FIM'
print('{:*^20}'.format(fim))
