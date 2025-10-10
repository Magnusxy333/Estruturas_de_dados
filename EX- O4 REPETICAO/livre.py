from random import randint
import sys

MENOR_POSSIVEL = 0
MAIOR_POSSIVEL = 10
TENTATIVAS_MAXIMAS = 5

def entrada_usuario(menor, maior):

    while True:
        try:

            entrada = input(f'Chute um número entre {menor} e {maior}: ')
            
            chute = int(entrada)
            
            if menor <= chute <= maior:
                return chute
            else:
                print(f"O número deve estar entre {menor} e {maior}. Tente novamente.")
        
        except ValueError:

            print('Entrada inválida! Digite apenas números inteiros.')


def sorteia_numero(menor, maior):
    return randint(menor, maior)


def jogar_adivinhe_o_numero():
    
    numero_sorteado = sorteia_numero(MENOR_POSSIVEL, MAIOR_POSSIVEL)
    
    tentativa_atual = 1

    print("-" * 30)
    print(f"Bem-vindo ao Adivinhe o Número!")
    print(f"Você tem {TENTATIVAS_MAXIMAS} chances para acertar o número secreto.")
    print("-" * 30)

    while tentativa_atual <= TENTATIVAS_MAXIMAS:
        
        print(f'\n--- Tentativa {tentativa_atual} de {TENTATIVAS_MAXIMAS} ---')
        
        chute = entrada_usuario(MENOR_POSSIVEL, MAIOR_POSSIVEL)

        if chute == numero_sorteado:
            print(f'\n🎉 **PARABÉNS!** Você acertou o número {numero_sorteado} em {tentativa_atual} tentativas!')
            return 

        elif chute > numero_sorteado:
            print('⬇Chute um número menor!')
        else: 
            print('⬆Chute um número maior!')
            
        tentativa_atual += 1

    print(f'\n--- FIM DE JOGO ---')
    print(f'VOCÊ PERDEU! Suas {TENTATIVAS_MAXIMAS} tentativas acabaram.')
    print(f'O número secreto era: **{numero_sorteado}**.')

if __name__ == "__main__":
    jogar_adivinhe_o_numero()