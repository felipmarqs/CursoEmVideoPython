print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
a = float(input('Qual o valor do primeiro segmento: '))
b = float(input('Qual o valor da segundo segmento: '))
c = float(input('Qual o valor da terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo!!')