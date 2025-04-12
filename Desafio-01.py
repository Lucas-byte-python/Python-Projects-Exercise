#01------------------------------------------------------------------------------
import time
print("Contagem regressiva para os fogos de artifício!")
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)
print("Estouro!")

#02------------------------------------------------------------------------------
print("Números pares de 1 a 50:")
for num in range(2, 51, 2):
    print(num, end=' ')

#03------------------------------------------------------------------------------
soma = 0
for num in range(1, 501):
    if num % 2 != 0 and num % 3 == 0:
        soma += num
print("A soma dos números ímpares múltiplos de 3 entre 1 e 500 é:", soma)

#04------------------------------------------------------------------------------
numero = int(input("Digite um número para ver a tabuada: "))
print(f"\nTabuada do {numero}:\n")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#05------------------------------------------------------------------------------
soma = 0
print("Digite 6 números inteiros:")
for i in range(1, 7):
    num = int(input(f"Digite o {i}º número: "))
    if num % 2 == 0:
        soma += num
print(f"\nA soma dos números pares é: {soma}")

#06------------------------------------------------------------------------------
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
print("\nOs 10 primeiros termos da PA são:")
for i in range(10):
    termo = primeiro + i * razao
    print(termo)

#07------------------------------------------------------------------------------
num = int(input("Digite um número inteiro: "))
divisores = 0
for i in range(1, num + 1):
    if num % i == 0:
        divisores += 1
if divisores == 2:
    print(f"\nO número {num} é primo.")
else:
    print(f"\nO número {num} NÃO é primo.")

#08------------------------------------------------------------------------------
frase = input("Digite uma frase: ").strip().lower()
frase_sem_espacos = frase.replace(" ", "")
inverso = frase_sem_espacos[::-1]
if frase_sem_espacos == inverso:
    print("\nÉ um palíndromo!")
else:
    print("\nNão é um palíndromo.")
