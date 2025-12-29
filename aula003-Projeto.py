print('''--------------------------------------------------------------------------
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            |.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           | .  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'|U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-|U|.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_|.-'
--------------------------------------------------------------------------''')

print('*BEM-VINDO A ILHA DO TESOURO*\n\n')
print('Sua missão é encontrar o tesouro perdido a partir de suas escolhas.\n\n')

escolha1 = input('O que voce escolher direita ou esquerda? ')
if escolha1 == "esquerda" or escolha1 == 'Esquerda':
    escolha2 = input('Você encontra um lago.\nO que você escolhe: nadar ou esperar? ')
    if escolha2 == 'esperar' or escolha2 == 'Esperar':
        escolha3 = input('Você chegou em uma ilha que possui três portas com as cores amarelo, vermelho e uma azul.\nQual você escolhe? ')
        if escolha3 == 'azul' or escolha3 =='Azul':
            print('Parabéns você encontrou o tesouro!!!')
        elif escolha3 == 'amarelo' or escolha3 == 'Amarelo':
            print('Você foi devorado por feras!\nGAME OVER')
        else:
            print('Você morreu queimado!\nGAME OVER')
    else:
        print('Você foi devorado por crocodilos!\nGAME OVER')
else:
    print('Você caiu em um buraco!\nGAME OVER')