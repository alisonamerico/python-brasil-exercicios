"""
12. Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58 
"""


def peso_ideal(altura: float) -> float:
    """Função que calcula o peso ideal
    
    Arguments:
        altura {float} -- Altura informada
    
    Returns:
        float -- retorna o peso ideal
    """
    peso = (72.7 * altura) - 58
    return peso


def test_peso_ideal() -> None:
    """test_peso_ideal(altura) -> resultado_esperado"""
    altura = 1.70
    resultado_esperado = 65.59
    assert round(peso_ideal(altura), 2) == resultado_esperado


if __name__ == "__main__":
    altura = float(input("Informe sua altura: "))
    print((f"O peso ideal para altura informa é: {peso_ideal(altura)}Kg"))
