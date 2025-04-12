#Estrutura de Repetição FOR---------------------------------------------
for c in range(0, 7, 2):
    print(c)
print('Fim')

for c in range(7, 0, +1):
    print(c)
print('Fim')

#Exemplo mais complexo---------------------------------------------------
n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)
print('Fim')

#Outro Exemplo-----------------------------------------------------------
i = int(input('Início: '))
f = int(input('Fim: '))
b = int(input('Passo: '))
for c in range(i, f+1, b):
    print(c)
print('Fim!')

#--------------------------------------------------------------------------
for c in range(0, 3):
    n = int(input("Digite um valor: "))
    print(n)
print("Fim!")

#--------------------------------------------------------------------------
s = 0
for c in range(0, 3):
    n = int(input("Digite um valor: "))
    s += n
print("O somatório de todos os valores foi {}".format(s))

#Exemplo Prático---------------------------------------------------------
for num in range (1000,10000):
    menor = num % 100 #obtem o numero dos algarismos menos significativos
    maior = num // 100 #obtem o numero dos algarismos mais significativos
    raiz = menor + maior  #obtem a raiz

    if (raiz * raiz ) == num: #valida se a raiz gera o numero testado
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print('terminou')
print('saiu ', num)

#Teste
start = int(1000 ** 0.5)

if start * start < 1000:
    start += 1

end = int(9999 ** 0.5)

for raiz in range(start, end + 1):
    num = raiz * raiz
    menor = num % 100
    maior = num // 100

    if (menor + maior) == raiz:
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print('terminou')
print('saiu ', raiz)