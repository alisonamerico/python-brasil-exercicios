"""
2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""


def imprime_valor_positivo_ou_negativo(valor: float) -> str:
    """Função que valida se número é positivo ou negativo.
    
    Arguments:
        valor {float} -- valor a ser validado.
    
    Returns:
        str -- Retorna valor esperado.
    """
    if valor > 0:
        return f"{valor} é positivo."
    elif valor < 0:
        return f"{valor} é negativo."
    return f"{valor} é Nulo."


def test_imprime_valor_positivo_ou_negativo() -> None:
    """assert imprime_valor_positivo_ou_negativo(valor) == valor_esperado"""
    valor = 8
    valor_esperado = f"{valor} é positivo."
    assert imprime_valor_positivo_ou_negativo(valor) == valor_esperado


if __name__ == "__main__":
    valor = float(input(f"Informe um valor: "))

    valor_esperado = imprime_valor_positivo_ou_negativo(valor)
    print(valor_esperado)
