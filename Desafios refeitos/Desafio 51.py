'''print('='*30)
print('{: ^30}'.format('10 termos de uma PA'))
print('='*30)
pt = int(input('Informe o primeiro termo: '))
r = int(input('Razão:'))
décimo = pt + (10-1) * r
for c in range(pt,décimo + r,r):
    print('{}'.format(c), end='→ ')
print('ACABOU')''''''
print('10 primeiros termos de uma PA')
pt = int(input('Informe o primeiro temo:'))
r = int(input('Informe a razão:'))
décimo = pt + (10-1) * r
for c in range(pt,décimo +r,r):
    print('{}'.format(c),end = '→ ')
print('Acabou')'''
pt = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão'))
décimo = pt + (10-1) * r
for c in range(pt,décimo + r,r):
    print('{}'.format(c),end= '→ ')
print('And thats all folks!')