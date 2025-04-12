#Exemplo 01
a = 10
for i in range(30):
    if a % 2 == 0:
        a += 1
        continue
    else:
        if a % 5 == 0:
            break
        else:
            a += 3
print(a)

#Exemplo 02
print("Olá mundo!")
print('7'+'4')
print(7+4)
print('7'+'4')
print("Olá", 5)

#Exemplo 03
nome = "Lucas"
idade = 24
peso = 74.0
print(nome,idade,peso)
#Exemplo de erro: print(nome+idade+peso)


nome = input("Qual seu nome?")
idade = input("Qual sua idade?")
peso = input("Qual seu peso?")
print(nome, idade, peso)

