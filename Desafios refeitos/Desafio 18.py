from math import cos,sin,tan,radians
#Faça um programa que lai um ânglo qualquer e mostre na tela o valor do sena, cosseno e tangente desse ângulo.
ang = int(input('Digite um ângulo para saber seu SENO, COSSENO E TANGENTE: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print(f'Considerando o ângulo {ang}º:')
print(f'O cosseno é {cosseno:.2f}.')
print(f'O seno é {seno:.2f}.')
print(f'O cosseno é {cosseno:.2f}.')
