"""
10. Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Farenheit. 

Fórmula:
°F = ((9 * °C) / 5) + 32

"""


def celsius_farenheit(valor_celsius: float) -> float:
    valor_farenheit = ((9 * valor_celsius) / 5) + 32
    return valor_farenheit


def test_celsius_farenheit() -> None:
    valor_entrada_celsius = 1
    valor_esperado_farenheit = 33.80000
    assert celsius_farenheit(valor_entrada_celsius) == valor_esperado_farenheit


if __name__ == "__main__":
    celsius = float(input("Informe uma temperatura em Celsius: "))
    print(f"A temperatura de {celsius}°C conrresponde a {celsius_farenheit(celsius)}°F")
