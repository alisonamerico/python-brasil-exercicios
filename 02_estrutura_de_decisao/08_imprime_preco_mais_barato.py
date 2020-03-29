"""
8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato. 
"""

from typing import List


lista_de_preco = []


def preco_produto_mais_barato(lista_de_preco: List[float]) -> float:
    """Função que verifica o produto com menor preço em uma lista.
    
    Arguments:
        lista_de_preco {List[float]} -- Lista a ser verificada.
    
    Returns:
        float -- Retorna o produto com menor preco.
    """
    return min(lista_de_preco)


def test_preco_produto() -> None:
    """assert preco_produto_mais_barato(lista_de_preco) -> preco_mais_barato"""
    lista_de_preco = [49.90, 170.00, 32.50]
    preco_mais_barato = 32.50
    assert preco_produto_mais_barato(lista_de_preco) == preco_mais_barato


if __name__ == "__main__":
    for indice in range(3):
        preco = float(input(f"Informe o {indice + 1}º produto: "))
        lista_de_preco.append(preco)

    preco_mais_barato = preco_produto_mais_barato(lista_de_preco)
    posicao = lista_de_preco.index(preco_mais_barato)

    print(f"O {posicao + 1}º produto possui o menor preço: R$ {preco_mais_barato}")
