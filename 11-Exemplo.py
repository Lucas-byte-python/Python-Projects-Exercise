#Importando Biblioteca de Problemas Matemáticos-----------
import math

x = math.sqrt(4)
print(x)

#Exemplo--------------------------------------------------
def calcular_raizes(a,b,c):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        return (raiz1, raiz2)
    elif delta == 0:
        raiz = -b / (2 * a)
        return (raiz,)
    else:
        parte_real = -b / (2 * a)
        parte_imaginaria = math.sqrt(-delta) / (2 * a)
        raiz1 = complex(parte_real, parte_imaginaria)
        raiz2 = complex(parte_real, -parte_imaginaria)
        return (raiz1, raiz2)

#Solicitar os coeficientes ao usuário
a = float(input("Digite um valor, please(A): "))
b = float(input("Digite um valor, please(B): "))
c = float(input("Digite um valor, please(C): "))

#Calculando as raizes
raizes = calcular_raizes(a, b, c)

#Resultado
if len(raizes) == 2:
    print(f'As raizes da equação são: {raizes[0]} e {raizes[1]}')
else:
    print(f'A raiz da equação é: {raizes[0]}')