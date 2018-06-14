#Faça um algoritimo que leia um preço de um produto e mostre seu novo preço, com 5% de desconto.
print('Na compra de qualquer produto você ganha 5% de desconto!!')
produto = float(input('Qual o preço do produto? '))
desconto = produto * 5/100
preçofinal = produto - desconto
print(f'Esse produto que custa R${produto:.2f} com o desconto de R${desconto:.2f} vai acabar custando R${preçofinal:.2f}  ')
