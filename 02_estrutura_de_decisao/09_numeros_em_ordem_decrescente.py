"""
9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

"""
Formas:

>>> L = [0,10,20,40]
>>> L[::-1]
[40, 20, 10, 0]

ou 

>>> L = [0,10,20,40]
>>> L.reverse()
>>> L
[40, 20, 10, 0]
"""


from typing import List


lista_numeros = []


def numeros_em_ordem_decrescente(lista_numeros: List[float]) -> List[float]:
    """Função que converte a uma lista para ordem decrescente.
    
    Arguments:
        lista_numeros {List[float]} -- Lista a ser verificada.
    
    Returns:
        List[float] -- Retorna uma lista em ordem reversa.
    """
    lista_em_ordem_decrescente = list(reversed(lista_numeros))
    return lista_em_ordem_decrescente


def test_numeros_em_ordem_decrescente() -> None:
    """assert numeros_em_ordem_decrescente(lista_numeros) -> lista_em_ordem_decrescente"""
    lista_numeros = [10, 20.0, 40]
    lista_em_ordem_decrescente = [40, 20.0, 10]
    assert numeros_em_ordem_decrescente(lista_numeros) == lista_em_ordem_decrescente


if __name__ == "__main__":
    for indice in range(3):
        numero = float(input(f"Informe {indice + 1}º número: "))
        lista_numeros.append(numero)
    lista_em_ordem_decrescente = numeros_em_ordem_decrescente(lista_numeros)
    print(f"Números em ordem decrescente são: {lista_em_ordem_decrescente}")
