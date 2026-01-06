from math import sqrt

def minha_funcao(a ,b, c):
    delta = b*b -4 * a * c

    if delta >= 0:
        x1 = (-b + sqrt(delta))/(2*b)
        x2 = (-b - sqrt(delta))/(2*b)
        print('x1 = ', x1)
        print('x2 = ', x2)
    else:
        print('Não possui raízes reais.')



a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

minha_funcao(a,b,c)