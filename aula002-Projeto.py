print('Bem-vindo a calculadora de gorjetas!')
valorTotal = float(input('Qual o total da sua conta? R$ '))
gorjeta = int(input('Quantos porcento de gorjeta voce gostaria de dar? '))
pessoas = int(input('Quantas pessoas irao dividir essa conta? '))

valorTotal += gorjeta/100 * valorTotal
valorPorPessoa = valorTotal/pessoas

print(f'Cada pessoa devera pagar: R$ {round(valorPorPessoa, 2)}')