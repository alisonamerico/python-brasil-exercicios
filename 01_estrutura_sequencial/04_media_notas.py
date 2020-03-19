"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média. 
"""


def media(nota1: float, nota2: float, nota3: float, nota4: float) -> float:
    """Função que soma 4 notas e exibe a média das mesmas.
    
    Arguments:
        nota1 {float} -- Primeiro nota
        nota2 {float} -- Segunda nota
        nota3 {float} -- Terceira nota
        nota4 {float} -- Quarta nota
    
    Returns:
        float -- Retorna a média das 4 notas.
    """
    return (nota1 + nota2 + nota3 + nota4) / 4


def test_media() -> None:
    assert round(media(7.5, 8, 9, 10), 1) == 8.6


if __name__ == "__main__":
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))
    nota4 = float(input("Informe a quarta nota: "))
    print()
    print(f"Média = {round(media(nota1, nota2, nota3, nota4), 1)}")
