tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('--Fim--')

#Exemplo Simplificado
tempo = int(input('Quantos anos tem seu carro?')),print('Carro Novo' if tempo <= 3 else 'Carro Velho'),print('Fim')

n1 = float(input('Digite nota 01:'))
n2 = float(input('Digite nota 02:'))
media = (n1+n2)/ 2
if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')