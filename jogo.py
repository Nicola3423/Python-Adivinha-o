import random

qtd_numeros = 5
min_valor = 1
max_valor = 10

def sorteia_numeros():
    numeros_sorteados = []
    while len(numeros_sorteados) < qtd_numeros:
        numero = random.randint(min_valor, max_valor)
        if numero not in numeros_sorteados:
            numeros_sorteados.append(numero)
    return numeros_sorteados

def pede_tentativas():
    tentativas = []
    while len(tentativas) < qtd_numeros:
        for i in range(1, qtd_numeros + 1):
            while True:
                    numero = int(input(f"\nDigite o {i}° número entre {min_valor} e {max_valor}: "))
                    if min_valor <= numero <= max_valor and numero not in tentativas:
                        tentativas.append(numero)
                        break
                    elif numero in tentativas:
                        print("Você já escolheu esse número. Escolha outro.")
                    else:
                        print(f"Por favor, digite um número entre {min_valor} e {max_valor}.")
    return tentativas

def verifica_acertos(numeros_sorteados, tentativas):
    acertos = set(numeros_sorteados) & set(tentativas)
    return acertos

def main():
    numeros_sorteados = sorteia_numeros()

    print("====> Bem-vindo ao jogo! <====")
    print("Tente adivinhar os 5 números entre 1 e 10")
    tentativas = pede_tentativas()

    acertos = verifica_acertos(numeros_sorteados, tentativas)

    print(f"\nNúmeros sorteados: {numeros_sorteados}")
    print(f"Suas tentativas: {tentativas}")
    print(f"Você acertou {len(acertos)} número(s): {acertos}")

if __name__ == "__main__":
    main()
