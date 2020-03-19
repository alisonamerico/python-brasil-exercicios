"""Faça um Programa que peça dois números e imprima a soma."""


def soma(numero1: int, numero2: int) -> int:
    """Função que retorna a soma de dois números
    
    Arguments:
        numero1 {int} -- Primeiro número
        numero2 {int} -- Segundo número
    
    Returns:
        int -- retorna a soma de dois números
    """
    return numero1 + numero2


def test_soma() -> None:
    assert soma(2, 4) == 6


if __name__ == "__main__":
    numero1 = int(input("Informe um número: "))
    numero2 = int(input("Informe outro número: "))
    print(soma(numero1, numero2))

