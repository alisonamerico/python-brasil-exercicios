"""
9. Faça um Programa que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus Celsius.

Fórmula:
    C = (5 * (F-32) / 9). 
"""


def farenheit_celsius(valor_farenheit: float) -> float:
    """Função que converte temperatura de Farenheit para graus Celsius
    
    Arguments:
        valor_farenheit {float} -- valor de temperatura em Farenheit
    
    Returns:
        float -- Retorna valor de temperatura em graus Celsius
    """
    valor_celsius = 5 * (valor_farenheit - 32) / 9
    return valor_celsius


def test_farenheit_celsius() -> None:
    """test_farenheit_celsius(valor_arenheit) -> valor_celsius"""
    valor_entrada_farenheit = 1
    valor_esperado_celsius = -17.22222222222222
    assert farenheit_celsius(valor_entrada_farenheit) == valor_esperado_celsius


if __name__ == "__main__":
    farenheit = float(input("Informe um valor temperatura em Farenheit: "))
    print(
        f"A temperatura convertida para graus Celsius é: {farenheit_celsius(farenheit)}"
    )
