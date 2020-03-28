"""
16. Faça um programa para uma loja de tintas. O programa deverá pedir o 
tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""


from math import ceil


def calcula_litros(tamanho_metro_quadrado: float) -> float:
    """Função que calcula a quantidade de litros por metro quadrado

    Arguments:
        tamanho_metro_quadrado {float} -- metro quadrado informado

    Returns:
        float -- Retorna a quantidade de litros por metro quadrado calculado.
    """
    litros = tamanho_metro_quadrado / 3
    return ceil(litros)


def test_litros() -> None:
    """calcula_litros(tamanho_metro_quadrado) -> litros_calculados"""
    tamanho_metro_quadrado = 200
    litros_calculados = 67

    assert calcula_litros(tamanho_metro_quadrado) == litros_calculados


def calcula_qtd_latas(tamanho_metro_quadrado: float) -> float:
    """Função que calcula quantidade de latas a serem usadas por metro quadrado.

    Arguments:
        tamanho_metro_quadrado {float} -- metro quadrado informado

    Returns:
        float -- Retorna a quantidade de latas por metro quadrado calculado.
    """
    capacidade_da_lata = 18
    latas = ceil(calcula_litros(tamanho_metro_quadrado) / capacidade_da_lata)
    return latas


def test_qtd_latas() -> None:
    """assert calcula_qtd_latas(tamanho_metro_quadrado) -> qtd_latas_calculadas"""
    tamanho_metro_quadrado = 200
    qtd_latas_calculadas = 4
    assert ceil(calcula_qtd_latas(tamanho_metro_quadrado)) == qtd_latas_calculadas


def calcula_preco_total(tamanho_metro_quadrado: float) -> float:
    """Função que calcula o preço total a ser pago

    Arguments:
        tamanho_metro_quadrado {float} -- metro quadrado informado

    Returns:
        float -- Retorna valor total a ser pago.
    """
    preco_lata = 80.00
    latas = calcula_qtd_latas(tamanho_metro_quadrado)
    preco_total = latas * preco_lata
    return preco_total


def test_preco_total() -> None:
    """assert calcula_preco_total(tamanho_metro_quadrado) -> preco_total_area_a_ser_pintada"""
    tamanho_metro_quadrado = 200
    preco_total_area_a_ser_pintada = 320
    assert calcula_preco_total(tamanho_metro_quadrado) == preco_total_area_a_ser_pintada


if __name__ == "__main__":
    tamanho_metro_quadrado = float(
        input(f"Quantos metros quadrados devem ser pintados: ")
    )
    latas = ceil(calcula_qtd_latas(tamanho_metro_quadrado))
    preco_total = ceil(calcula_preco_total(tamanho_metro_quadrado))

    print()

    if latas > 1:
        print(f"Você usará {latas} latas de tinta")
    else:
        print(f"Você usará {latas} lata de tinta")
    print(f"O preço total é de: R$ {preco_total}")
