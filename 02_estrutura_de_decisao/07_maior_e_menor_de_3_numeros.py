"""
6. Faça um Programa que leia três números e mostre o maior e o menor deles. 
"""

from typing import List


lista_numeros = []


def calcula_maior_de_3_numeros(lista_numeros: List[float]) -> float:
    """Função que verifica o maior número dentro de uma lista.
    
    Arguments:
        lista_numeros {List[float]} -- Lista com números a serem verifcados.
    
    Returns:
        float -- Retorna o maior número da lista.
    """
    return max(lista_numeros)


def test_maior_de_3_numeros() -> None:
    """assert calcula_maior_de_3_numeros(lista_numeros) -> maior_numero_da_lista"""
    lista_numeros = [6.0, 9.3, 30]
    maior_numero_da_lista = 30
    assert calcula_maior_de_3_numeros(lista_numeros) == maior_numero_da_lista


def calcula_menor_de_3_numeros(lista_numeros: List[float]) -> float:
    """Função que verifica o menor número dentro de uma lista.
    
    Arguments:
        lista_numeros {List[float]} -- Lista com números a serem verifcados.
    
    Returns:
        float -- Retorna o menor número da lista.
    """
    return min(lista_numeros)


def test_menor_de_3_numeros() -> None:
    """assert calcula_menor_de_3_numeros(lista_numeros) -> maior_numero_da_lista"""
    lista_numeros = [4.0, 81, 9.0]
    maior_numero_da_lista = 4
    assert calcula_menor_de_3_numeros(lista_numeros) == maior_numero_da_lista


if __name__ == "__main__":
    for indice in range(3):
        numero = float(input(f"Informe o {indice + 1}° número: "))
        lista_numeros.append(numero)

    maior_numero = calcula_maior_de_3_numeros(lista_numeros)
    menor_numero = calcula_menor_de_3_numeros(lista_numeros)
    print()
    print(f"{maior_numero} É o maior número.")
    print(f"{menor_numero} É o menor número.")
