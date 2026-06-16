# infra-cache-performance
Experimental evaluation of memory hierarchy performance on Intel Core i5-1235U

# 📊 Infra Cache Performance

## Influência do Tamanho do Conjunto de Dados na Largura de Banda da Hierarquia de Memória

Este projeto investiga como o tamanho do conjunto de dados impacta a largura de banda de memória em um processador Intel Core i5-1235U, explorando o comportamento da hierarquia de cache (L1, L2, L3) e memória RAM.

---

## 🎯 Objetivo

Analisar como diferentes tamanhos de dados afetam o desempenho de operações de cópia de memória, medindo a largura de banda observada.

---

## 🧠 Hipótese

- **H0:** O tamanho do conjunto de dados não influencia a largura de banda.
- **H1:** O aumento do conjunto de dados reduz a largura de banda ao ultrapassar caches.

---

## ⚙️ Metodologia

- Linguagem: Python 3.11
- Biblioteca: NumPy
- Métrica: Largura de banda (MB/s)
- Operação: cópia de arrays em memória
- Tamanhos testados:
  - 1 MB, 4 MB, 8 MB, 16 MB, 32 MB, 64 MB, 128 MB, 256 MB
- Execuções:
  - 35 execuções por cenário
  - 5 warm-up descartadas
  - 30 medições válidas

---

## 📈 Resultados

Os resultados mostram:

- Alta performance para dados pequenos (cache L1/L2)
- Queda progressiva ao ultrapassar cache L3
- Estabilização em tamanhos maiores (uso de RAM)

---

## 📊 Gráficos

Os gráficos gerados mostram:

- Relação entre tamanho do dataset e bandwidth
- Variabilidade das medições (desvio padrão)

📌 Local: `results/plots/`

---

## 🧪 Como executar

```bash
pip install -r requirements.txt
python src/benchmark.py
python src/analysis.py