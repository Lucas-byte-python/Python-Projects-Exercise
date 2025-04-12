#Exemplo base recursivo------------------------------
def regressiva(x):
   print(x)
   regressiva(x - 1)

#Exemplo recursivo-----------------------------------
def regressiva(x):
   if x <= 0:
        print("Acabou")
   else:
        print(x)
        regressiva(x-1)

# Exemplo recursivo contagem regressiva-----------------------------------
def regressiva(x):
    print(x)
    if x > 0:
       regressiva(x-1)
    else:
       print('Acabou')
regressiva(10)
print('\n')

#Exemplo não recursivo-----------------------------------------------
for y in range (10, -1, -1):
    print(y)
print('Cabou','\n')

#Exemplo recursivo Fatorial--------------------------
def fatorial(n):
    if n == 0 or n == 1:
         return 1
    else:
         return n*fatorial(n-1)

#Exemplo com teste Fatorial--------------------------
def fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        for x in range(2, n + 1):
           fat = fat*x
        return fat

#Teste Base de determinar o n-ésimo termo da sequência de Fibonacci Exemplo------------
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

#Determina o n-ésimo termo da sequência de Fibonacci Exemplo------------
def fibo(n):
   'Determina o n-ésimo termo da sequência de Fibonacci'
   if n == 1 or n == 2:
      return 1
   else:
      return fibo(n - 1) + fibo(n = 2)
vfibo = fibo(5)
print(vfibo)
print('\n')
print(help(fibo))
