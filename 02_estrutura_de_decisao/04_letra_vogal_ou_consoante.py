"""
4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""


def valida_letra_se_eh_vogal_ou_consoante(letra: str) -> str:
    """Função que verifica se letra informada é uma vogal ou consoante.
    
    Arguments:
        letra {str} -- letra a ser verificada.
    
    Returns:
        str -- Retorna uma vogal ou consoante.
    """
    vogais = ["a", "e", "i", "o", "u"]
    if letra.strip().lower() in vogais:
        return f"{letra.strip()} é uma vogal."
    else:
        return f"{letra.strip()} é uma consoante."


def test_valida_letra_se_eh_vogal_ou_consoante() -> None:
    """assert valida_letra_se_eh_vogal_ou_consoante(letra) -> letra_esperada"""
    letra = "a"
    letra_esperada = f"{letra.strip()} é uma vogal."
    assert valida_letra_se_eh_vogal_ou_consoante(letra) == letra_esperada


if __name__ == "__main__":
    letra = input("Informe uma letra: ")

    letra_esperada = valida_letra_se_eh_vogal_ou_consoante(letra)
    print(letra_esperada)
