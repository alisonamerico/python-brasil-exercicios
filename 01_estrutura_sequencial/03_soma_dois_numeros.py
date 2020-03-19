"""Faça um Programa que peça dois números e imprima a soma."""


def soma(numero1: int, numero2: int) -> int:
    return numero1 + numero2


def test_soma() -> None:
    assert soma(2, 4) == 6


if __name__ == "__main__":
    numero1 = int(input("Informe um número: "))
    numero2 = int(input("Informe outro número: "))
    print(soma(numero1, numero2))

