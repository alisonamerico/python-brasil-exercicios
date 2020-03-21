"""
7. Faça um Programa que calcule a área de um quadrado, 
em seguida mostre o dobro desta área para o usuário. 
"""

"""
Fórmula:

Para calcular a área do quadrado, basta multiplicar a medida de dois lados 
(l) dessa figura. Muitas vezes os lados são chamados de base (b) e altura (h).
No quadrado a base é igual à altura (b=h). Logo, temos a fórmula da área:

A = L2
ou
A = b.h

"""


def area_quadrado(base: int, altura: int) -> int:
    """Função que mostra o dobro da área do quadrado.
    
    Arguments:
        base {int} -- valor da base do quadrado
        altura {int} -- valor da altura do quadrado
    
    Returns:
        int -- retorna o dobro da área do quadrado.
    """
    area_dobro = (base * altura) * 2
    return area_dobro


def test_area_quadrado() -> None:
    """test_area_quadrado(2, 2) -> 8"""
    valor_entrada_base = 2
    valor_entrada_altura = 2
    valor_esperado = 8
    assert area_quadrado(valor_entrada_base, valor_entrada_altura) == valor_esperado


if __name__ == "__main__":
    base = 4
    altura = 4
    print(f"Dobro área do quadrado é: {area_quadrado(base, altura)}")
