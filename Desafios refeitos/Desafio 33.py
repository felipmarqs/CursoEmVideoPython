#Faça um programa que leia trÊs número e mostre qual é o maior e qual é o menor.
a = int(input('1º número:'))
b = int(input('2º número:'))
c = int(input('3º número:'))
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o menor
print('O menor valor digitado foi {}'.format(menor))
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
# Verificando quem é o maior
print('O maior valor digitado foi {}'.format(maior))
