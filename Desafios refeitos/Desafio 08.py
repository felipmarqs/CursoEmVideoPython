#Escreva um programa que leia um valor em metros e exiba covertido em centímetros e milímetros.
m = float(input('Quantos metros queres converter ?'))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f'{m} metros equivalem à:  ')
print(f'{km:.2f} Kilômetros ')
print(f'{hm:.2f} Hectômetros ')
print(f'{dam:.2f} Decâmetros ')
print(f'{dm:.2f} Decímetros ')
print(f'{cm:.2f} Centímetros ')
print(f'{mm:.2f} Milímetros ')
