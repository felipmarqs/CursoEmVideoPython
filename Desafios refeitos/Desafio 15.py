#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
#por dia e R$0.15 por KM rodado
print('Bom dia viajante!')
km = int(input('Quantos KM você rodou com o carro? KM'))
dias = int(input('Com quantos dias você ficou com o carro? '))
aluguel = (dias * 60) + (km*0.15)
print('Considerando que você deve pagar R$60 por cada dia e R$0.15 por KM rodado:')
print(f'Você ficou com o carro por {dias} dias e rodou {km}KM, por isso terá que pagar R${aluguel}')