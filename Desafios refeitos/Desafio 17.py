from math import sqrt
#Faça um programa que leia o comprimento do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
CO = float(input('Qual o comprimento do cateto oposto? '))
CA = float(input('QUal o comprimento do cateto adjacente? '))
H = sqrt(CO ** 2 + CA **2)
print(f'O valor da hipotenusa é {H:.2f}')