"""
17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor. 

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 
"""


from math import ceil


def calcula_litros(tamanho_metro_quadrado: float) -> float:
    """Função que calcula a quantidade de litros por metro quadrado

    Arguments:
        tamanho_metro_quadrado {float} -- metro quadrado informado

    Returns:
        float -- Retorna a quantidade de litros por metro quadrado calculado.
    """
    litros = (tamanho_metro_quadrado / 6) * 0.1
    if litros <= 0:
        litros = 1
    return ceil(litros)


def test_litros() -> None:
    """calcula_litros(tamanho_metro_quadrado) -> litros_calculados"""
    tamanho_metro_quadrado = 200
    litros_calculados = 4

    assert calcula_litros(tamanho_metro_quadrado) == litros_calculados


def calcula_qtd_latas_18_litros(tamanho_metro_quadrado: float) -> int:
    """Função que calcula quantidade de latas de 18 litros a serem usadas por metro quadrado.

    Arguments:
        tamanho_metro_quadrado {float} -- metro quadrado informado

    Returns:
        float -- Retorna a quantidade de latas de 18 litros por metro quadrado calculado.
    """
    capacidade_da_lata = 18
    latas = ceil(calcula_litros(tamanho_metro_quadrado) / capacidade_da_lata)
    return latas  # 1


def test_qtd_latas_18_litros() -> None:
    """assert calcula_qtd_latas_18(tamanho_metro_quadrado) -> qtd_latas_calculadas"""
    tamanho_metro_quadrado = 200
    qtd_latas_calculadas = 1
    assert (
        round(calcula_qtd_latas_18_litros(tamanho_metro_quadrado))
        == qtd_latas_calculadas
    )


def calcula_qtd_galao_3_6_litros(tamanho_metro_quadrado: float) -> float:
    """Função que calcula quantidade de 3.6 galões a serem usadas por metro quadrado.

    Arguments:
        tamanho_metro_quadrado {float} -- metro quadrado informado

    Returns:
        float -- Retorna a quantidade de 3.6 galões por metro quadrado calculado.
    """
    capacidade_do_galao = 3.6
    galoes = calcula_litros(tamanho_metro_quadrado) / capacidade_do_galao
    return ceil(galoes)


def test_qtd_galao_3_6_litros() -> None:
    """assert calcula_qtd_galoes_3_6(tamanho_metro_quadrado) -> qtd_latas_calculadas"""
    tamanho_metro_quadrado = 200
    qtd_galoes_calculados = 2
    assert (
        round(calcula_qtd_galao_3_6_litros(tamanho_metro_quadrado))
        == qtd_galoes_calculados
    )


def calcula_preco_lata_18_litros(tamanho_metro_quadrado: float) -> float:
    """Função que calcula o preço da lata de 18 litros.

    Arguments:
        tamanho_metro_quadrado {float} -- metro quadrado informado

    Returns:
        float -- Retorna preço da lata de 18 litros a ser pago.
    """
    preco_lata = 80.0
    latas = calcula_qtd_latas_18_litros(tamanho_metro_quadrado)
    preco_total = latas * preco_lata
    return preco_total


def test_preco_lata_18_litros() -> None:
    """assert calcula_preco_lata_18_litros(tamanho_metro_quadrado) -> preco_total_area_a_ser_pintada"""
    tamanho_metro_quadrado = 200
    preco_total_area_a_ser_pintada = 80
    assert (
        round(calcula_preco_lata_18_litros(tamanho_metro_quadrado), 2)
        == preco_total_area_a_ser_pintada
    )


def calcula_preco_galao_3_6_litros(tamanho_metro_quadrado: float) -> float:
    """Função que calcula o preço do galão de 3.6 litros.

    Arguments:
        tamanho_metro_quadrado {float} -- metro quadrado informado

    Returns:
        float -- Retorna preço do galão de 3.6 litros a ser pago.
    """
    preco_galao = 25.00
    galao = calcula_qtd_galao_3_6_litros(tamanho_metro_quadrado)
    preco_total = galao * preco_galao
    return preco_total


def test_preco_lata_3_6_litros() -> None:
    """assert calcula_preco_galao_3_6_litros(tamanho_metro_quadrado) -> preco_total_area_a_ser_pintada"""
    tamanho_metro_quadrado = 200
    preco_total_area_a_ser_pintada = 50
    assert (
        round(calcula_preco_galao_3_6_litros(tamanho_metro_quadrado), 2)
        == preco_total_area_a_ser_pintada
    )


def calcula_valor_total_misto(tamanho_metro_quadrado: float) -> float:
    """Função que calcula o valor total da soma entre latas e galões.

    Arguments:
        tamanho_metro_quadrado {float} -- tamanho do metro quadrado

    Returns:
        float -- valor total calculado da soma entre latas e galões
    """
    valor_misto = calcula_preco_lata_18_litros(
        tamanho_metro_quadrado
    ) + calcula_preco_galao_3_6_litros(tamanho_metro_quadrado)
    return valor_misto


def test_valor_total_misto() -> None:
    """assert (calcula_valor_total_misto(tamanho_metro_quadrado) -> valor_total_misto_calculado"""
    tamanho_metro_quadrado = 200
    valor_total_misto_calculado = 130
    assert (
        round(calcula_valor_total_misto(tamanho_metro_quadrado), 2)
        == valor_total_misto_calculado
    )


if __name__ == "__main__":
    tamanho_metro_quadrado = float(
        input(f"Quantos metros quadrados devem ser pintados: ")
    )
    latas_18_litros = ceil(calcula_qtd_latas_18_litros(tamanho_metro_quadrado))
    preco_lata_18_litros = calcula_preco_lata_18_litros(tamanho_metro_quadrado)
    galao_3_6_litros = ceil(calcula_qtd_galao_3_6_litros(tamanho_metro_quadrado))
    preco_galao_3_6_litros = calcula_preco_galao_3_6_litros(tamanho_metro_quadrado)
    valor_total_misto = calcula_valor_total_misto(tamanho_metro_quadrado)

    print()
    if latas_18_litros <= 0 or galao_3_6_litros <= 0:
        latas_18_litros = 1
        galao_3_6_litros = 1

    if latas_18_litros > 1:
        print(
            f"O preço de {latas_18_litros} latas de tinta de 18 litros, custam: R$ {round(preco_lata_18_litros, 2)}"
        )
    else:
        print(
            f"O preço de {latas_18_litros} lata de tinta de 18 litros, custa: R$ {round(preco_lata_18_litros, 2)}"
        )

    print()

    if galao_3_6_litros > 1:
        print(
            f"O preço de {galao_3_6_litros} galões de tinta de 3.6 litros, custam: R$ {round(preco_galao_3_6_litros, 2)}"
        )
    else:
        print(
            f"O preço de {galao_3_6_litros} galão de tinta de 3.6 litros, custa: R$ {round(preco_galao_3_6_litros, 2)}"
        )

    print()

    print(f"Valor total misto (latas + galões): R$ {round(valor_total_misto, 2)}")
