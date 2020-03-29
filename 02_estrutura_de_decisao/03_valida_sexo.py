"""
3. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""


def valida_sexo(letra: str) -> str:
    """Função que valida sexo.
    
    Arguments:
        letra {str} -- letra a ser validada.
    
    Returns:
        str -- Retorna "Masculino", "Feminino" ou "Sexo Inválido."
    """
    if letra.upper() == "M":
        return "Masculino"
    elif letra.upper() == "F":
        return "Feminino"
    else:
        return "Sexo Inválido"


def test_valida_sexo() -> None:
    letra = "M"
    valor_esperado = "Masculino"
    assert valida_sexo(letra) == valor_esperado


if __name__ == "__main__":
    letra = input("Informe 'F' para Feminino ou 'M' para Masculino: ")

    valor_esperado = valida_sexo(letra)
    print(valor_esperado)
