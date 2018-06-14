#Desenvolva um programa que pergunte a distância em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200KM e R$0,45
#para viagens mais longas
d = float(input('Qual a distância da viagem:'))
print('Você está prestes a começar sua viagem de {d} Km')
'''if d <= 200:
    preço = d * 0.50
    print('O preço da sua passagem será de R$ {:.2f}.'.format(preço))
else:
    preço = d * 0.45
    print('O preço da sua passagem será de R$ {:.2f}'.format(preço))'''
preço = d * 0.50 if d <= 200 else d * 0.45
print(f'E o preço da sua passagem será de R$ {preço:.2f}')