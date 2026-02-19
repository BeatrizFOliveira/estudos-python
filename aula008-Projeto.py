#CIFRA DE CESAR
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def criptografar(mensagem, num):
    palavraCripto = ""
    for i in mensagem:
        for j in range(len(letras)):
            if i == letras[j]:
                palavraCripto += letras[(j + num)%26]
                break

    print(f"\nPalavra descriptografada: " + palavraCripto)



def descriptografar(mensagem, num):
    palavraDescripto = ""
    for i in mensagem:
        for j in range(len(letras)):
            if i == letras[j]:
                palavraDescripto += letras[(j - num)%26]
                break

    print(f"\nPalavra descriptografada: " + palavraDescripto)


op = True
while(op == True):
    
    acao = input("\nDigite 'CODIFICAR' para criptografar e 'DECODIFICAR' para descriptografar.\n").upper()
    mensagem = input("\nDigite sua mensagem: ").upper()
    num = int(input("\nDigite o número de codificação: "))

    if acao == "CODIFICAR":
        criptografar(mensagem, num)
    elif acao == "DECODIFICAR":
        descriptografar(mensagem, num)
    else:
        print("\nVALOR INVÁLIDO!\n")

    continuar = input("\nDigite SIM se você quer iniciar novamente. Caso contrário digite NÃO.\n").upper()
    if continuar == 'NÃO' or continuar == 'NAO':
        op = False
    