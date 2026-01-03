import random

ascii_art = ["""\n    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)\n""","""\n     _______\n---'    ____)____\n           ______)\n          _______)\n         _______)\n---.__________)\n""","""\n    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)\n"""]

opcao_escolhida = int(input('Escolha:\n 1) Pedra \n 2) Papel \n 3) Tesoura\n\nQual você escolhe? '))

if 0 > opcao_escolhida > 2:
    print('Opcao inválida')
else:
    print('Sua escolha:\n', ascii_art[opcao_escolhida-1])

    escolha_computador = random.randint(0, 2) + 1
    print('O computador escolheu: ', ascii_art[escolha_computador-1])

    if escolha_computador == opcao_escolhida:
        print('EMPATE')
    elif opcao_escolhida == (escolha_computador+1) or (opcao_escolhida == 1 and escolha_computador == 3):
        print('VOCÊ GANHOU!!!')
    else:
        print('GAME OVER')


    
