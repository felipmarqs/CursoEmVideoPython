from datetime import date
print('''[1] Se você for homem
      [2] Se for mulher''')
op = int(input('Você '))
atual = date.today().year
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda falta(m) {} ano(s) para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}'.format(atual + saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você tem {} anos, deveria ter se alistado há {} anos.'.format(idade,saldo))
    print('Seu alistamento foi em {}.'.format(atual - saldo))
