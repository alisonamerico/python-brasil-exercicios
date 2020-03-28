"""
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    a. o produto do dobro do primeiro com metade do segundo .
    b. a soma do triplo do primeiro com o terceiro.
    c. o terceiro elevado ao cubo. 
"""

import math


def dobro_do_primeiro_com_metade_do_segundo(
    primeiro_numero: int, segundo_numero: int
) -> int:
    """Função que recebe dois números e retorna o produto
     do dobro do primeiro com metade do segundo.
    
    Arguments:
        primeiro_numero {int} -- Primeiro número informado
        segundo_numero {int} -- Segundo número informado
    
    Returns:
        int -- Retorna o produto do dobro do primeiro com metade do segundo
    """
    resultado = (2 * primeiro_numero) + (segundo_numero // 2)
    return resultado


def test_dobro_do_primeiro_com_metade_do_segundo() -> None:
    """test_dobro_primeiro_com_metade_segundo(valor_entrada_1, valor_entrada_2) -> resultado_esperado"""
    valor_entrada_1 = 2
    valor_entrada_2 = 4
    resultado_esperado = 6
    assert (
        dobro_do_primeiro_com_metade_do_segundo(valor_entrada_1, valor_entrada_2)
        == resultado_esperado
    )


def soma_triplo_do_primeiro_com_terceiro(
    primeiro_numero: int, numero_real: float
) -> float:
    """Função que soma do triplo do primeiro com o terceiro(numero real).
    
    Arguments:
        primeiro_numero {int} -- Primeiro número informado
        numero_real {float} -- Número real informado
    
    Returns:
        float -- Retorna a soma do triplo do primeiro com o terceiro
    """
    resultado_1 = (primeiro_numero * 3) + numero_real
    return resultado_1


def test_soma_triplo_do_primeiro_com_terceiro() -> None:
    """test_soma_triplo_do_primeiro_com_terceiro(primeiro_numero, numero_real) -> resultado_esperado_1"""
    primeiro_numero = 2
    numero_real = 8
    resultado_esperado_1 = 14
    assert (
        soma_triplo_do_primeiro_com_terceiro(primeiro_numero, numero_real)
        == resultado_esperado_1
    )


def terceiro_elevado_ao_cubo(numero_real: float) -> float:
    """Função que exibe um número elevado ao cubo.
    
    Arguments:
        numero_real {float} -- Número real informado
    
    Returns:
        float -- Retorna o número real elevado ao cubo
    """
    numero_ao_cubo = math.pow(numero_real, 3)
    return numero_ao_cubo


def test_terceiro_elevado_ao_cubo() -> None:
    """terceiro_elevado_ao_cubo(numero_real) -> resultado_esperado_2"""
    numero_real = 6
    resultado_esperado_2 = 216
    assert terceiro_elevado_ao_cubo(numero_real) == resultado_esperado_2


if __name__ == "__main__":
    primeiro_numero = int(input("Informe um número: "))
    segundo_numero = int(input("Informe outro número: "))
    numero_real = float(input("Informe um número real: "))
    print(
        f"O produto do dobro do primeiro com metade do segundo é: {dobro_do_primeiro_com_metade_do_segundo(primeiro_numero, segundo_numero)}"
    )
    print(
        f"A soma do triplo do primeiro com o terceiro é: {soma_triplo_do_primeiro_com_terceiro(primeiro_numero, numero_real)}"
    )
    print(f"O terceiro elevado ao cubo é: {terceiro_elevado_ao_cubo(numero_real)}")
