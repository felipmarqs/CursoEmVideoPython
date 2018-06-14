#Faça um programa que leia a velocidade um carro.
#SE ele ultrapassar 8km/h, moste uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada KM acima do limite.
velocidade = float(input('Digite a velocidade do seu carro em Km/h '))
multa = (velocidade - 80) * 7.0
if velocidade >= 80:
    print('Você excedeu o limite de 80Km/h você terá que pagar uma multa de {:.2f} R$'.format(multa))
print('Tenha um bom dia! Dirija com segurança')