"""
5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

  * A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
  * A mensagem "Reprovado", se a média for menor do que sete;
  * A mensagem "Aprovado com Distinção", se a média for igual a dez.

"""


lista_notas = []


def calcula_media_aluno(lista_notas: list) -> float:
    """Função que calcula a média de duas notas de um aluno.

    Arguments:
        lista_notas {list} -- Lista com as duas notas

    Returns:
        float -- Retorna a média
    """
    media = sum(lista_notas) / len(lista_notas)
    return media


def test_media() -> None:
    """assert calcula_media_aluno(lista_notas) -> media"""
    lista_notas = [8, 10]
    media = 9
    assert calcula_media_aluno(lista_notas) == media


if __name__ == "__main__":

    for indice in range(2):
        nota = float(input(f"Informe a {indice + 1}ª nota: "))
        lista_notas.append(nota)

    media = calcula_media_aluno(lista_notas)

    if 7 <= media < 10:
        print(f"A média do aluno foi de {media}: Aprovado")
    elif media < 7:
        print(f"A média do aluno foi de {media}: Reprovado")
    elif media == 10:
        print("Aprovado com distinção")


# def calcula_media_aluno(nota1: float, nota2: float) -> float:
#     """Função que calcula a média de duas notas de um aluno.

#     Arguments:
#         nota1 {float} -- Primeira nota
#         nota2 {float} -- Segunda nota

#     Returns:
#         float -- Retorna a média
#     """
#     media_aluno = (nota1 + nota2) / 2
#     return media_aluno


# def test_media_aluno() -> None:
#     """assert calcula_media_aluno(nota1, nota2) == media_aluno"""
#     nota1 = 7.5
#     nota2 = 10
#     media_aluno = 8.75
#     assert calcula_media_aluno(nota1, nota2) == media_aluno


# if __name__ == "__main__":

#     nota1 = float(input(f"Informe a 1ª nota: "))
#     nota2 = float(input(f"Informe a 2ª nota: "))

#     media = calcula_media_aluno(nota1, nota2)

#     if 7 <= media < 10:
#         print(f"A média do aluno foi de {media}: Aprovado")
#     elif media < 7:
#         print(f"A média do aluno foi de {media}: Reprovado")
#     elif media == 10:
#         print("Aprovado com distinção")
