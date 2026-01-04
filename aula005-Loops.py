#Estruturas de repetição: WHILE-----------------------------
x = 0
while(x < 3):
    print(x)
    x += 1

i = 1
while i <= 10:
    if i == 5:
        break #Ao usar o break o laço é interrompido e o while finaliza.
    print(i)
    i += 1

i = 0
while i < 5:
    i += 1

    if i == 3:
        continue #Ao usar o continue, o programa ignora o restando do while e vai para o próximo laço.

    print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i é maior que 6") #Da mesma forma que o if também pode ser colocado um else quando o while for finalizado.


#É possível usar o break, continue e else também no laço FOR
#Estrutura de Repetição: FOR--------------------------------

frutas = ['Maça', 'Banana', 'Laranja']
for frutas in frutas:
    print(frutas)

for i in range(2, 10):
    print(i)

for i in range(1, 10, 2): #Ao colocar um terceiro parâmetro no for isso será o valor do incremento
    print(i)

for i in 'banana':
    print(i)


