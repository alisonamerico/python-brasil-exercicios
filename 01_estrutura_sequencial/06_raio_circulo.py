"""
6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. 
"""

"""
Fórmula:

Área = Pi * raio²

A = Pi * r²

"""
import math


def raio_circulo(raio: float):
    area = math.pi * (raio ** 2)
    return area


def test_raio_circulo() -> None:
    assert round(raio_circulo(2), 2) == 12.57


if __name__ == "__main__":
    raio = float(input("Informe um valor o raio do circulo: "))
    print(f"Área do circulo: {round(raio_circulo(raio), 2)} m²")

