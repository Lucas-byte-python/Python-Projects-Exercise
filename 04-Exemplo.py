#Estrutura Condicional Simples
nome=str(input('Qual é o seu nome?'))
if nome == 'Lucas':
    print('Nome Padão!')
print('Tenha um bom dia, {}'.format(nome))

#Estrutura Condicional Composta
nome=str(input('Qual é o seu nome?'))
if nome == 'Lucas':
    print('Nome Padão!')
else:
    print('Belo Nome')
print('Tenha um bom dia, {}'.format(nome))

#Estrutura Condicional Alinhada
nome=str(input('Qual é o seu nome?'))
if nome == 'Lucas':
    print('Nome Padão!')
elif nome == 'João' or nome == 'Maria' or nome == 'Gustavo':
    print('Nome popular')
else:
    print('Belo Nome')
print('Tenha um bom dia, {}'.format(nome))

#Estrutura Condicional Alinhada 02
nome=str(input('Qual é o seu nome?'))
if nome == 'Lucas':
    print('Nome Padão!')
elif nome == 'João' or nome == 'Maria' or nome == 'Gustavo':
    print('Nome popular')
elif nome in 'Ana Cladia Luiza Beatriz Keliane':
    print('Mulheres')
else:
    print('Belo Nome')
print('Tenha um bom dia, {}'.format(nome))