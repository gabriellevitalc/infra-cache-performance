import pandas as pd
import numpy as np

# Carregar dados
df = pd.read_csv("dados/resultados_memoria.csv")

# Remover warm-up (primeiras 5 execuções)
df = df[df["repeticao"] > 5]

resultado = []

for tamanho in sorted(df["tamanho_mb"].unique()):

    grupo = df[df["tamanho_mb"] == tamanho]

    media = grupo["largura_banda_mb_s"].mean()
    desvio = grupo["largura_banda_mb_s"].std()

    n = len(grupo)

    erro = 1.96 * (desvio / np.sqrt(n))

    ic_inf = media - erro
    ic_sup = media + erro

    resultado.append([
        tamanho,
        round(media, 2),
        round(desvio, 2),
        round(ic_inf, 2),
        round(ic_sup, 2)
    ])

tabela = pd.DataFrame(
    resultado,
    columns=[
        "Tamanho_MB",
        "Media_MB_s",
        "Desvio_Padrao",
        "IC95_Inferior",
        "IC95_Superior"
    ]
)

print(tabela)

tabela.to_csv(
    "resultados_estatisticos.csv",
    index=False
)

print("\nArquivo resultados_estatisticos.csv gerado com sucesso!")