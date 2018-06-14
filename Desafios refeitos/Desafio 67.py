while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    for t in range(1,11):
        print(f'{num} X {t} = {num*t}')
print('Programa encerrado!')