#01---------------------------------------------------
def calcula_imc(peso, altura):
    return peso * 100 / (altura * 2)

peso = eval(input('Digite o seu peso em quilos: '))
altura = eval(input('Digite sua altura em centimetros: '))

calcula_imc(peso, altura)
imc = calcula_imc(peso, altura)
print('Imc: ', imc, '\n')

#02---------------------------------------------------
def taximetro(distancia, multiplicador=1):
    largarda = 3
    km_rodado = 2
    valor = (largarda + distancia * km_rodado) * multiplicador
    return valor

pagamento = taximetro(3.5)
print(pagamento, '\n')

#03--------------------------------------------------
def func1(x):
    x = 10
    print(f'Função func1 - x = {x}')

def func2(x):
    x = 20
    print(f'Função func2 - x = {x}')
    return x

vn = 0
print(f'Programa principal - vn = {vn}')
vn = func1(vn)
print(f'Programa principal - vn = {vn}')
vn = func2(vn)
print(f'Programa principal - x = {vn}\n')

#04---------------------------------------------------------
def func1():
    global x
    x = 10
    print(f'Função func1 - x = {x}')

def func2():
    global x
    x = 20
    print(f'Função func2 - x = {x}')

x = 0
func1()
func2()
print(f'Programa principal - x = {x}')

#05-----------------------------------------------------------
def taximetro(distancia):
    def calculaMult():
        if distancia < 5:
            return 1.2
        else:
            return 1

    multiplicador = calculaMult()
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor

dist = eval(input("Entre com a distancia a ser percorrida em km: \n"))
pagamento = taximetro(dist)
print(f'O valor a pagar é R$ {pagamento}')