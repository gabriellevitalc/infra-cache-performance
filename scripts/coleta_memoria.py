import numpy as np
import time
import csv

tamanhos_mb = [1, 4, 8, 16, 32, 64, 128, 256]

resultados = []

for tamanho in tamanhos_mb:

    tamanho_bytes = tamanho * 1024 * 1024

    for repeticao in range(35):

        origem = np.ones(tamanho_bytes // 8, dtype=np.float64)
        destino = np.zeros_like(origem)

        inicio = time.perf_counter()

        np.copyto(destino, origem)

        fim = time.perf_counter()

        tempo = fim - inicio

        largura_banda = tamanho / tempo

        resultados.append(
            [tamanho, repeticao + 1, largura_banda]
        )

with open("dados/resultados_memoria.csv", "w", newline="") as arquivo:

    writer = csv.writer(arquivo)

    writer.writerow(
        ["tamanho_mb", "repeticao", "largura_banda_mb_s"]
    )

    writer.writerows(resultados)

print("Coleta concluída.")
