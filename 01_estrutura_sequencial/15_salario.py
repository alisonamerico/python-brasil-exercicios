"""
15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido. 
"""


def calcula_salario_bruto(
    valor_hora_trabalhada: float, qtd_horas_trabalhadas_mes: float
) -> float:
    """Função que calcula o salário bruto no mês.
    
    Arguments:
        valor_hora_trabalhada {float} -- Valor da hora trabalhada
        qtd_horas_trabalhadas_mes {float} -- Quantidade de horas trabalhadas por mês
    
    Returns:
        float -- Valor do salário bruto no mês
    """
    salario_bruto_no_mes = valor_hora_trabalhada * qtd_horas_trabalhadas_mes
    return salario_bruto_no_mes


def test_salario_bruto() -> None:
    """salario_bruto(valor_hora_trabalhada, qtd_horas_trabalhadas_mes)
        -> salario_bruto_no_mes
    """
    valor_hora_trabalhada = 15
    qtd_horas_trabalhadas_mes = 160
    salario_bruto_no_mes = 2400
    assert (
        calcula_salario_bruto(valor_hora_trabalhada, qtd_horas_trabalhadas_mes)
        == salario_bruto_no_mes
    )


def calcula_imposto_renda(
    valor_hora_trabalhada: float, qtd_horas_trabalhadas_mes: float
) -> float:
    """Função que calcula o imposto de renda.
    
    Arguments:
        valor_hora_trabalhada {float} -- Valor da hora trabalhada por mês.
        qtd_horas_trabalhadas_mes {float} -- Quantidade de horas trabalhadas no mês
    
    Returns:
        float -- Valor do Imposto de Renda calculado.
    """
    imposto_renda = (
        calcula_salario_bruto(valor_hora_trabalhada, qtd_horas_trabalhadas_mes) * 0.11
    )
    return imposto_renda


def test_imposto_renda() -> None:
    """calcula_imposto_renda(valor_hora_trabalhada, qtd_horas_trabalhadas_mes) -> valor_imposto_renda"""
    valor_imposto_renda = 264.0
    valor_hora_trabalhada = 15
    qtd_horas_trabalhadas_mes = 160
    assert (
        calcula_imposto_renda(valor_hora_trabalhada, qtd_horas_trabalhadas_mes)
        == valor_imposto_renda
    )


def calcula_inss(
    valor_hora_trabalhada: float, qtd_horas_trabalhadas_mes: float
) -> float:
    """Função que calcula o INSS.
    
    Arguments:
        valor_hora_trabalhada {float} -- Valor da hora trabalhada por mês.
        qtd_horas_trabalhadas_mes {float} -- Quantidade de horas trabalhadas no mês
    
    Returns:
        float -- Valor do INSS calculado.
    """
    inss = (
        calcula_salario_bruto(valor_hora_trabalhada, qtd_horas_trabalhadas_mes) * 0.08
    )
    return inss


def test_inss() -> None:
    """calcula_inss(valor_hora_trabalhada, qtd_horas_trabalhadas_mes) -> valor_inss"""
    valor_inss = 192.0
    valor_hora_trabalhada = 15
    qtd_horas_trabalhadas_mes = 160
    assert calcula_inss(valor_hora_trabalhada, qtd_horas_trabalhadas_mes) == valor_inss


def calcula_sindicato(
    valor_hora_trabalhada: float, qtd_horas_trabalhadas_mes: float
) -> float:
    """Função que calcula o Sindicato.
    
    Arguments:
        valor_hora_trabalhada {float} -- Valor da hora trabalhada por mês.
        qtd_horas_trabalhadas_mes {float} -- Quantidade de horas trabalhadas no mês
    
    Returns:
        float -- Valor do Sindicato calculado.
    """
    inss = (
        calcula_salario_bruto(valor_hora_trabalhada, qtd_horas_trabalhadas_mes) * 0.05
    )
    return inss


def test_sindicato() -> None:
    """calcula_sindicato(valor_hora_trabalhada, qtd_horas_trabalhadas_mes) -> valor_sindicato"""
    valor_sindicato = 120.0
    valor_hora_trabalhada = 15
    qtd_horas_trabalhadas_mes = 160
    assert (
        calcula_sindicato(valor_hora_trabalhada, qtd_horas_trabalhadas_mes)
        == valor_sindicato
    )


def calcula_salario_liquido(
    valor_hora_trabalhada: float, qtd_horas_trabalhadas_mes: float
) -> float:
    """Função que calcula o Salário Líquido.
    
    Arguments:
        valor_hora_trabalhada {float} -- Valor da hora trabalhada por mês.
        qtd_horas_trabalhadas_mes {float} -- Quantidade de horas trabalhadas no mês
    
    Returns:
        float -- Valor do Salário Líquido calculado.
    """
    descontos = (
        calcula_imposto_renda(valor_hora_trabalhada, qtd_horas_trabalhadas_mes)
        + calcula_inss(valor_hora_trabalhada, qtd_horas_trabalhadas_mes)
        + calcula_sindicato(valor_hora_trabalhada, qtd_horas_trabalhadas_mes)
    )

    salario_bruto = calcula_salario_bruto(
        valor_hora_trabalhada, qtd_horas_trabalhadas_mes
    )
    salario_liquido = salario_bruto - descontos
    return salario_liquido


def test_salario_liquido() -> None:
    """calcula_salario_liquido(valor_hora_trabalhada, qtd_horas_trabalhadas_mes) -> salario_liquido"""
    salario_liquido = 1824.0
    valor_hora_trabalhada = 15
    qtd_horas_trabalhadas_mes = 160
    assert (
        calcula_salario_liquido(valor_hora_trabalhada, qtd_horas_trabalhadas_mes)
        == salario_liquido
    )


if __name__ == "__main__":
    valor_hora_trabalhada = float(input("Informe quanto voce recebe por hora: "))
    qtd_horas_trabalhadas_mes = float(input("Quantas horas voce trabalhou no mês: "))
    print()
    salario_bruto = calcula_salario_bruto(
        valor_hora_trabalhada, qtd_horas_trabalhadas_mes
    )
    imposto_renda = calcula_imposto_renda(
        valor_hora_trabalhada, qtd_horas_trabalhadas_mes
    )
    inss = calcula_inss(valor_hora_trabalhada, qtd_horas_trabalhadas_mes)

    sindicato = calcula_sindicato(valor_hora_trabalhada, qtd_horas_trabalhadas_mes)

    salario_liquido = calcula_salario_liquido(
        valor_hora_trabalhada, qtd_horas_trabalhadas_mes
    )

    print(f"Salário Bruto: {salario_bruto}")
    print(f"Imposto de Renda: {imposto_renda}")
    print(f"INSS: {inss}")
    print(f"Sindicato: {sindicato}")
    print(f"Salário Liquido: {salario_liquido}")
