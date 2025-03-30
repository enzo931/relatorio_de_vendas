# 📊 Sistema de Análise de Vendas com Gráficos e Relatórios

Este é um projeto completo desenvolvido em Python que analisa arquivos Excel contendo dados de vendas, gera relatórios detalhados, gráficos variados e permite filtros por período. Ideal para controle financeiro simples, visualização de desempenho de produtos e análise de faturamento diário.

---

## ✅ Funcionalidades

- 📥 Leitura automática de arquivos `.xlsx`
- 📆 Filtro por intervalo de datas
- 💸 Cálculo de:
  - Total de faturamento
  - Média de faturamento por dia
  - Top 3 produtos mais vendidos
  - Dia com maior faturamento
- 📊 Geração de gráficos:
  - Gráfico de **barras** (Faturamento por produto)
  - Gráfico de **pizza** (Distribuição do faturamento)
  - Gráfico de **linha** (Faturamento ao longo do tempo)
- 💾 Exportação:
  - Relatório detalhado em `.txt`
  - Gráficos salvos automaticamente em `.png` (alta resolução)

---

## 📁 Exemplo de Estrutura do Excel

| Data       | Produto     | Quantidade | Preço Unitário |
|------------|-------------|------------|----------------|
| 2024-01-01 | Teclado RGB | 5          | 150.00         |
| 2024-01-01 | Mouse Gamer | 8          | 80.00          |
| ...        | ...         | ...        | ...            |

---

## ▶️ Como Executar

1. Certifique-se de ter o Python instalado (versão 3.8 ou superior).
2. Instale as bibliotecas necessárias (caso ainda não tenha):

pip install pandas matplotlib openpyxl

Coloque seu arquivo Excel (ex: vendas.xlsx) na mesma pasta do script.

Execute o programa no terminal:

python relatorio_vendas_completo.py

📤 Arquivos Gerados

relatorio_geral.txt → resumo geral do faturamento

grafico_barras.png → faturamento por produto (barras)

grafico_pizza.png → distribuição de faturamento

grafico_linha.png → evolução do faturamento ao longo do tempo
