print('----- CIFRA DE CÉSAR -----')

base_minuscula = 'abcdefghijklmnopqrstuvwxyz'
base_maiuscula = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
tamanho_base = len(base_minuscula)

def codificar (t, c):
    texto_final = ''

    for letra in t:
        if letra in base_minuscula:
            posicao = base_minuscula.find(letra)
            posicao += c

            if posicao >= tamanho_base:
                posicao -= tamanho_base

            texto_final += base_minuscula[posicao]

        elif letra in base_maiuscula:
            posicao = base_maiuscula.find(letra)
            posicao += c

            if posicao >= tamanho_base:
                posicao -= tamanho_base
                    
            texto_final += base_maiuscula[posicao]

        else:
            texto_final += letra         

    return (texto_final)


def decodificar(t, c):
    texto_final = ''

    for letra in t:
        if letra in base_minuscula:
            posicao = base_minuscula.find(letra)
            posicao -= c

            if posicao < 0:
                posicao += tamanho_base

            texto_final += base_minuscula[posicao]

        elif letra in base_maiuscula:
            posicao = base_maiuscula.find(letra)
            posicao -= c

            if posicao < 0:
                posicao += tamanho_base
                    
            texto_final += base_maiuscula[posicao]

        else:
            texto_final += letra       


    return (texto_final)


modo = int(input('Codificar - 1\nDecodificar - 2\n\nQual você deseja? (1 / 2): '))

if modo != 1 and modo != 2:
    print('Entrada inválido. Tente novamente.')

else:
    texto = input('Digite o texto para converter: ')
    chave = int(input('Digite a chave desejada (deslocamento para direita [0 - 25]): '))

    if chave < 0 or chave > 25:
        print('Chave inválida. Tente novamente.')
    
    else:
 
        if modo == 1:
            texto_final = codificar(texto, chave)
            print(f'Texto codificado:\n{texto_final}')

        elif modo == 2:
            texto_final = decodificar(texto, chave)
            print(f'Texto decodificado:\n{texto_final}')