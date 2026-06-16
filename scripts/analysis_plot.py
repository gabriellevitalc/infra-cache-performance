import pandas as pd
import matplotlib.pyplot as plt
import os

# garante pastas
os.makedirs("figuras", exist_ok=True)

# carregar dados
df = pd.read_csv("dados/resultados_memoria.csv")

# remover warm-up (mesma lógica da sua análise estatística)
df = df[df["repeticao"] > 5]

# agrupar por tamanho
grupo = df.groupby("tamanho_mb")["largura_banda_mb_s"]

media = grupo.mean()
desvio = grupo.std()

# ----------------------------
# GRÁFICO 1: LARGURA DE BANDA
# ----------------------------
plt.figure()
plt.plot(media.index, media.values, marker="o")

plt.title("Largura de Banda vs Tamanho do Conjunto de Dados")
plt.xlabel("Tamanho (MB)")
plt.ylabel("Largura de Banda (MB/s)")
plt.grid()

plt.savefig("figuras/bandwidth_vs_size.png")
plt.close()

# ----------------------------
# GRÁFICO 2: DESVIO PADRÃO
# ----------------------------
plt.figure()
plt.plot(desvio.index, desvio.values, marker="o")

plt.title("Variabilidade da Largura de Banda")
plt.xlabel("Tamanho (MB)")
plt.ylabel("Desvio Padrão (MB/s)")
plt.grid()

plt.savefig("figuras/std_vs_size.png")
plt.close()

print("Gráficos gerados com sucesso!")