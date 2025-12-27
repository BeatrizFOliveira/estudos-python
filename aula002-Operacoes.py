nome = 'Ana'
peso = 52
altura = 1.65
status = True

print(type(nome))
print(type(peso))
print(type(altura))
print(type(status))

IMC = peso/(altura**2)

print(IMC)
print(int(IMC)) #Transforma o número em inteiro
arredondado = round(IMC, 2) #Arredonda o número com duas casas decimais de precisão

print(f'Seu IMC é de {arredondado}')

