"""
1. Faça um Programa que mostre a mensagem "Alo mundo" na tela. 

"""


def alo_mundo() -> str:
    """Função que exibe a mensagem "Alo mundo".
    
    Returns:
        str -- "Alo mundo"
    """
    return "Alo mundo"


def test_alo_mundo() -> None:
    assert alo_mundo() == "Alo mundo"


if __name__ == "__main__":
    print()
    print(alo_mundo())
