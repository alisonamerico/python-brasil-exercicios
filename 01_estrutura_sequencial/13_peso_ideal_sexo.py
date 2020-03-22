"""
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 
"""


def peso_ideal_homem(altura: float) -> float:
    """Função que calcula o peso ideal do homem
    
    Arguments:
        altura {float} -- Altura informada
    
    Returns:
        float -- retorna o peso ideal do homem
    """
    peso_homem = (72.7 * altura) - 58
    return peso_homem


def test_peso_ideal_homem() -> None:
    """peso_ideal_homem(altura) -> resultado_esperado"""
    altura_homem = 1.70
    resultado_esperado = 65.59
    assert round(peso_ideal_homem(altura_homem), 2) == resultado_esperado


def peso_ideal_mulher(altura: float) -> float:
    """Função que calcula o peso ideal da mulher
    
    Arguments:
        altura {float} -- Altura informada
    
    Returns:
        float -- retorna o peso ideal da mulher
    """
    peso_mulher = (62.1 * altura) - 44.7
    return peso_mulher


def test_peso_ideal_mulher() -> None:
    """peso_ideal_mulher(altura) -> resultado_esperado"""
    altura_mulher = 1.60
    resultado_esperado = 54.66
    assert round(peso_ideal_mulher(altura_mulher), 2) == resultado_esperado


if __name__ == "__main__":
    altura = float(input("Informe sua altura: "))
    print(
        (
            f"O peso ideal para o homem com base na altura informa é: {round(peso_ideal_homem(altura), 2)}Kg"
        )
    )
    print(
        (
            f"O peso ideal para a mulher com base na altura informa é: {round(peso_ideal_mulher(altura), 2)}Kg"
        )
    )
