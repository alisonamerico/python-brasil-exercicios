"""
14. João Papo-de-Pescador, homem de bem, comprou um microcomputador 
para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido 
pelo regulamento de pesca do estado de São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável 
peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite
e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas. 
"""


def calcula_excesso(peso: float, peso_maximo_estabelecido: float) -> float:
    """Função que calcula a quantidade de peixes maior que o estabelecido 
       pelo regulamento de pesca do estado de São Paulo (50 quilos) 
    
    Arguments:
        peso {float} -- Quantidade de quilos de peixes pescados
        peso_maximo_estabelecido {float} -- Quantidade de quilos máximos permitidos.
    
    Returns:
        float -- Retorna a quantidade de quilos excedidos.
    """
    peso_maximo_estabelecido = 50
    excesso = peso - peso_maximo_estabelecido
    return excesso


def test_calcula_excesso() -> None:
    """calcula_excesso(peso, peso_maximo_estabelecido) -> valor_esperado_excesso"""
    peso = 54
    peso_maximo_estabelecido = 50
    valor_esperado_excesso = 4
    assert calcula_excesso(peso, peso_maximo_estabelecido) == valor_esperado_excesso


def calcula_multa(
    multa_por_quilo_excedente: float, peso: float, peso_maximo_estabelecido: float
) -> float:
    """Função que calcula o valor da multa por quilo de peixe excedido
       pelo estado de São Paulo.
    
    Arguments:
        multa_por_quilo_excedente {float} -- Valor da multa por quilo excedido.
        excesso {float} -- Quantidade de quilos excedidos
    
    Returns:
        float -- Retorna o valor total da multa a ser paga.
    """
    multa_por_quilo_excedente = 4
    multa = multa_por_quilo_excedente * calcula_excesso(peso, peso_maximo_estabelecido)
    return multa


def test_calcula_multa() -> None:
    """calcula_multa(multa_por_quilo_excedente, peso) -> valor_esperado_multa"""
    peso = 54
    peso_maximo_estabelecido = 50
    multa_por_quilo_excedente = 4.00
    valor_esperado_multa = 16.00
    assert (
        calcula_multa(multa_por_quilo_excedente, peso, peso_maximo_estabelecido)
        == valor_esperado_multa
    )


if __name__ == "__main__":
    peso = float(input("Quantos quilos de peixes foram pescados: "))

    peso_maximo_estabelecido = 50.00
    excesso = calcula_excesso(peso, peso_maximo_estabelecido)
    multa_por_quilo_excedente = 4
    multa = calcula_multa(multa_por_quilo_excedente, peso, peso_maximo_estabelecido)

    if peso > peso_maximo_estabelecido:
        print(
            f"""Peso informado: {peso}Kg, ultrapassou o peso estabelecido
             pelo regulamento de pesca do estado de São Paulo (50 quilos), 
             deverá pagar uma multa de R$ 4,00 por quilo excedente. """
        )
        print(f"Total da multa: {multa} reais.")
    else:
        print(
            f"""Peso informado {peso}Kg, está em conformidade com o regulamento
             de pesca do estado de São Paulo (50 quilos)"""
        )
