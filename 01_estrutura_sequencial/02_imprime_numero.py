"""
2. Faça um Programa que peça um número e então mostre a mensagem 
'O número informado foi [número].' 

"""

# Versão isolando input:
def pede_numero(numero: int) -> str:
    """Função que solicita um número e retorna uma mensagem com
     o número informado.
    
    Arguments:
        numero {int} -- Número informado 
    
    Returns:
        str -- Mensagem informando o número digitado.
    """
    return f"O número informado foi {numero}"


def test_pede_numero() -> None:
    assert pede_numero(1) == "O número informado foi 1"


if __name__ == "__main__":
    pede_numero(int(input("Informe um número: ")))


# # Versão 2 com input mocado. Nem usei a lib:
# def pede_numero() -> str:
#     numero = int(input("Informe um número: "))
#     return f"O número informado foi {numero}"


# def test():
#     global input

#     def input_mocado(s):
#         return 1

#     input = input_mocado
#     assert pede_numero() == "O número informado foi 1"

