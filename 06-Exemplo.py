#01----------------------------------------------------
def diz_ola():
    print("Olá, Mundo!")

#02---------------------------------------------------
escolha = input("Escolha uma opção de função: 1 ou 2\n")
if escolha == "1":
    def func1(x):
        return x + 1
    s = func1(10)
else:
    def func2(x):
        return x + 2
    s = func2(10)
print(s)

