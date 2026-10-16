"""
Pedra, Papel, Tesoura, Lagarto, Spock
Baseado no jogo popularizado pela série The Big Bang Theory

Regras:
- Tesoura corta Papel
- Papel cobre Pedra
- Pedra esmaga Lagarto
- Lagarto envenena Spock
- Spock quebra Tesoura
- Tesoura decapita Lagarto
- Lagarto come Papel
- Papel refuta Spock
- Spock vaporiza Pedra
- Pedra amassa Tesoura
"""

import random

# Dicionário de regras: cada chave vence as opções listadas em seu valor,
# junto com a frase explicativa usada no resultado.
REGRAS = {
    "pedra": {
        "tesoura": "Pedra amassa Tesoura",
        "lagarto": "Pedra esmaga Lagarto",
    },
    "papel": {
        "pedra": "Papel cobre Pedra",
        "spock": "Papel refuta Spock",
    },
    "tesoura": {
        "papel": "Tesoura corta Papel",
        "lagarto": "Tesoura decapita Lagarto",
    },
    "lagarto": {
        "spock": "Lagarto envenena Spock",
        "papel": "Lagarto come Papel",
    },
    "spock": {
        "tesoura": "Spock quebra Tesoura",
        "pedra": "Spock vaporiza Pedra",
    },
}

OPCOES = list(REGRAS.keys())

ATALHOS = {
    "1": "pedra",
    "2": "papel",
    "3": "tesoura",
    "4": "lagarto",
    "5": "spock",
}


def exibir_menu():
    print("\nEscolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("4 - Lagarto")
    print("5 - Spock")
    print("0 - Sair")


def obter_escolha_jogador():
    while True:
        exibir_menu()
        escolha = input("Sua escolha: ").strip().lower()

        if escolha == "0":
            return None

        if escolha in ATALHOS:
            return ATALHOS[escolha]

        if escolha in OPCOES:
            return escolha

        print("Opção inválida! Tente novamente.")


def obter_escolha_computador():
    return random.choice(OPCOES)


def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "empate", None

    if computador in REGRAS[jogador]:
        return "jogador", REGRAS[jogador][computador]

    return "computador", REGRAS[computador][jogador]


def jogar():
    print("=" * 50)
    print(" PEDRA, PAPEL, TESOURA, LAGARTO, SPOCK ")
    print(" (The Big Bang Theory) ")
    print("=" * 50)

    placar = {"jogador": 0, "computador": 0, "empate": 0}

    while True:
        escolha_jogador = obter_escolha_jogador()

        if escolha_jogador is None:
            break

        escolha_computador = obter_escolha_computador()

        print(f"\nVocê escolheu: {escolha_jogador.capitalize()}")
        print(f"Computador escolheu: {escolha_computador.capitalize()}")

        resultado, explicacao = determinar_vencedor(escolha_jogador, escolha_computador)

        if resultado == "empate":
            print("Empate!")
        elif resultado == "jogador":
            print(f"Você venceu! ({explicacao})")
        else:
            print(f"COMPUTADOR VENCEU! ({explicacao})")

        placar[resultado] += 1

        print(f"\nPlacar -> Você: {placar['jogador']} | "
              f"Computador: {placar['computador']} | "
              f"Empates: {placar['empate']}")

    print("\n" + "=" * 50)
    print("Placar final:")
    print(f"Você: {placar['jogador']}")
    print(f"Computador: {placar['computador']}")
    print(f"Empates: {placar['empate']}")

    if placar["jogador"] > placar["computador"]:
        print("\nParabéns, você venceu no geral! 🎉")
    elif placar["jogador"] < placar["computador"]:
        print("\nO computador venceu no geral. Tente novamente!")
    else:
        print("\nNo geral, ficou empatado!")

    print("Obrigado por jogar!")


if __name__ == "__main__":
    jogar()
