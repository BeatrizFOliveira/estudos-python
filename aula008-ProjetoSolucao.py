#Essa é a solução do curso. Ficou muita parecida com a minha, mas vale apresentar alguns detalhes:
# 1. Foi usado array ao invés de uma string, o que permitiu usar o método index (que eu não conhecia)
# 2. As função de criptografar e descriptografar foram unidas em uma única função, sendo usado a múltiplicação por -1 para mudar para descriptografia.


alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def criptografar(mensagem, num):
#     palavraCripto = ""
#     for i in mensagem:
#         posNum = alfabeto.index(i) + num #O MÉTODO INDEX SERVE PARA ACHAR UM VALOR EM UMA LISTA

#         posNum %= len[alfabeto]
#         palavraCripto += alfabeto[posNum]

#     print(f"\nPalavra criptografada: {palavraCripto}")

# def descriptografar(mensagem, num):
#     palavraDescripto = ""
#     for i in mensagem:
#         posNum = alfabeto.index(i) - num #O MÉTODO INDEX SERVE PARA ACHAR UM VALOR EM UMA LISTA

#         posNum %= len[alfabeto]
#         palavraDescripto += alfabeto[posNum]

#     print(f"\nPalavra descriptografada: {palavraDescripto}")


#USO CRIPTOGRAFAR E DESCRIPTOGRAFAR EM UMA ÚNICA FUNÇÃO
def cesar(mensagem, num, acao):
    textoSaida = ""

    if acao == 'decodificar':
        num *= -1
        
    for i in mensagem:
        if i not in alfabeto:
            textoSaida += i

        else:

            posNum = alfabeto.index(i) + num #O MÉTODO INDEX SERVE PARA ACHAR UM VALOR EM UMA LISTA
            posNum %= len(alfabeto)
            textoSaida += alfabeto[posNum]

    print(f"\nResultado: {textoSaida}")
        

op = True
while op:
    acao = input("\nDigite 'CODIFICAR' para criptografar e 'DECODIFICAR' para descriptografar.\n").lower()
    mensagem = input("\nDigite sua mensagem: ").lower()
    num = int(input("\nDigite o número de codificação: "))

    cesar(mensagem, num, acao)

    recomecar = input("\nDigite 'sim' se você quer continuar. Caso contrário digite 'não': ").lower()
    if recomecar == 'não' or recomecar == 'nao':
        op = False