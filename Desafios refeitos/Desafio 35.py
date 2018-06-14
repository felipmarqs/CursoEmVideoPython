#Desenvolva um programa que leia o comprimento de três retas
#e diga ao usuário se elas podem ou não formar um triângulo.

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
a = float(input('Qual o valor do primeiro segmento: '))
b = float(input('Qual o valor da segundo segmento: '))
c = float(input('Qual o valor da terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos PODEM FORMAR um triângulo!!')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo!!')