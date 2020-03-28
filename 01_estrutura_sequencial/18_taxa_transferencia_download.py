"""
18. Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).
"""


def calcula_tempo_download(
    tamanho_arquivo: float, velocidade_de_download: float
) -> float:
    velocidade_em_bits = velocidade_de_download / 8
    tempo = (tamanho_arquivo / velocidade_em_bits) / 60
    return round(tempo, 2)


def test_tempo_download() -> None:
    tamanho_arquivo = 200
    velocidade_de_download = 15
    tempo_download_calculado = 1.78
    assert (
        calcula_tempo_download(tamanho_arquivo, velocidade_de_download)
        == tempo_download_calculado
    )


if __name__ == "__main__":
    tamanho_arquivo = float(input("Informe o tamanho do arquivo em MB: "))
    velocidade_de_download = int(input("Informe a velocidade do download em Mbps: "))

    tempo = calcula_tempo_download(tamanho_arquivo, velocidade_de_download)

    print(f"O tempo de Download será de aproximadamente {tempo} minutos")
