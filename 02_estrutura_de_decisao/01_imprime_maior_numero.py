"""
1. Faça um Programa que peça dois números e imprima o maior deles.
"""


def imprime_maior_numero(numero1: int, numero2: int) -> int:
    maior_numero = numero1
    if numero2 > maior_numero:
        maior_numero = numero2
    return maior_numero


def test_imprime_maior_numero() -> None:
    numero1 = 2
    numero2 = 4
    maior_numero = numero2
    assert imprime_maior_numero(numero1, numero2) == maior_numero


if __name__ == "__main__":
    numero1 = int(input("Informe um número: "))
    numero2 = int(input("Informe outro número: "))
    maior_numero = imprime_maior_numero(numero1, numero2)
    print(f"O maior número é: {maior_numero}")

    # lista = []
    # for numero in range(2):
    #     numero = int(input(f"Informe o {numero + 1}° número:"))
    #     lista.append(numero)
    # print()
    # print(f"O maior número é: {max(lista)}")
