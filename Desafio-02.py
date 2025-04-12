#01---------------------------------------------------------------------------------
def encontrar_maior_elemento_iterativo(lista):
  """
  Encontra o maior elemento em uma lista de números inteiros de forma não recursiva.

  Args:
    lista: A lista de números inteiros.

  Returns:
    O maior elemento da lista.
  """

  if len(lista) <= 1:
    # Caso base: se a lista tiver no máximo 1 elemento, ele é o maior
    return lista[0]

  maior_elemento = lista[0]
  for numero in lista[1:]:
    if numero > maior_elemento:
      maior_elemento = numero

  return maior_elemento

# Exemplo de uso
lista_exemplo = [7, 2, 55, 1, 4, 3, 6]
maior_elemento = encontrar_maior_elemento_iterativo(lista_exemplo)
print(f"O maior elemento da lista é: {maior_elemento}")
print()

#02----------------------------------------------------------------------------------
def rec(n):
  if n < 2:
    return n
  return rec(n - 1)

print('Subtraindo até: ',rec(5))
print()

#03----------------------------------------------------------------------------------
def encontrar_maior_elemento_nao_recursivo(lista):
  """
  Encontra o maior elemento em uma lista de números inteiros de forma não recursiva.

  Args:
    lista: A lista de números inteiros.

  Returns:
    O maior elemento da lista.
  """

  if len(lista) <= 1:
    # Caso base: se a lista tiver no máximo 1 elemento, ele é o maior
    return lista[0]

  maior_elemento = lista[0]
  for numero in lista[1:]:
    if numero > maior_elemento:
      maior_elemento = numero

  return maior_elemento

# Exemplo de uso
lista_exemplo = [7, 2, 5, 25, 4, 3, 6]
maior_elemento = encontrar_maior_elemento_nao_recursivo(lista_exemplo)
print(f"O maior elemento da lista é: {maior_elemento}")
print()

#04----------------------------------------------------------------------
import math
n = 5.9
print('O menor valor inteiro maior ou igual ao número 5.9 é: ',math.ceil(n))

#05----------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox


def comp_numeros():
  num1 = float(entry_num1.get())
  num2 = float(entry_num2.get())

  if num1 > num2:
    messagebox.showinfo("Resultado", f"O numero {num1} é maior que {num2}")
  elif num1 == num2:
    messagebox.showinfo("Resultado", f"O numero {num1} é  igual a {num2}")
  else:
    messagebox.showinfo("Resultado", f"O numero {num1} é menor que {num2}")

# Criando a janela----------------------------------------------------------
janela = tk.Tk()
janela.title("Comparando Numeros")

# Criando os widgets--------------------------------------------------------
label_num1 = tk.Label(janela, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(janela, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_num2 = tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

botao_comp = tk.Button(janela, text="Comparar", command=comp_numeros)
botao_comp.grid(row=2, columnspan=2, padx=10, pady=5)

# Rodando o loop principal---------------------------------------------------
janela.mainloop()

#Method 02-------------------------------------------------------------------
def comp_numeros():
  try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if num1 > num2:
      print(f"O número {num1} é maior que {num2}.")
    elif num1 == num2:
      print(f"O número {num1} é igual a {num2}.")
    else:
      print(f"O número {num1} é menor que {num2}.")
  except ValueError:
    print("Por favor, digite apenas números válidos.")


# Executando o programa
comp_numeros()