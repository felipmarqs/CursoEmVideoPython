#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
num = int(input('Digite um número de 0 à 9999: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print(f'''Uidade: {unidade}
Dezena: {dezena}
Centena: {centena}
Milhar: {milhar}''')