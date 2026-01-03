import random

#.randint gera um número inteiro entre um intervalo
num_aleatorio = random.randint(1, 10)
print(num_aleatorio)

#.random gera um número entre 0 e 1
num_aleatorio2 = random.random()
print(num_aleatorio2)

#.uniform gera um número float entre dois valores
num_aleatorio3 = random.uniform(1.3, 1.5)
print(num_aleatorio3)


#.choice escolhe um dos elementos da lista
amigos = ['Ana', 'Bia', 'Caio', 'Edu']
print(random.choice(amigos))

