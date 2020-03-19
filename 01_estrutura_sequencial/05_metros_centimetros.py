"""
5. Faça um Programa que converta metros para centímetros.
"""

"""
Regra de conversão:
1m == 100cm

Metro para centímetro:      
cm = metro x 100

"""


def metros_centimetros(metro: float) -> float:
    """Função que converte metros em centímetros.
    
    Arguments:
        metro {float} -- número em metro
    
    Returns:
        float -- número convertido em centímentros.
    """
    return metro * 100


def test_metros_centimetros() -> None:
    assert metros_centimetros(5) == 500


if __name__ == "__main__":
    metro = float(input("Informe um número (metro): "))
    print(f"Valor: {metros_centimetros(metro)}cm")
