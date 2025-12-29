altura = int(input('Qual sua altura em cm? '))
idade = int(input('Qual sua idade? '))
valorTotal = 0

if altura >= 120:
    print('\nVocê pode andar na montanha-russa')
    if idade <= 12:
        valorTotal = 10
    elif idade <=18:
        valorTotal = 12
    elif idade >= 45 and idade <= 55:
        valorTotal = 0
    else:
        valorTotal = 15
    print(f'\nO valor do ingresso é de R${valorTotal}')

    foto = input('\nVocê deseja foto? (Digite: S para sim e N para não) ')
    if foto == 's' or foto == 'S':
        valorTotal += 3
    
    print(f'\nO valor total da conta será de R$ {valorTotal}')
    
else:
    print('\nVocê não tem altura suficiente para andar na montanha russa.')