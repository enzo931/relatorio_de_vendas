import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# ========== CONFIGURAÇÕES ==========
ARQUIVO_EXCEL = 'vendas.xlsx'
EXPORTAR_RELATORIO_TXT = True
EXPORTAR_GRAFICOS = True

# ========== LEITURA DOS DADOS ==========
df = pd.read_excel(ARQUIVO_EXCEL)

# Verifica se a coluna de data está no formato datetime
df['Data'] = pd.to_datetime(df['Data'])

# Cálculo de Faturamento
df['Faturamento'] = df['Quantidade'] * df['Preço Unitário']

# ========== FILTRO POR DATA ==========
filtrar = input("Deseja filtrar por data? (s/n): ").lower()
if filtrar == 's':
    inicio = input("Digite a data de início (YYYY-MM-DD): ")
    fim = input("Digite a data de fim (YYYY-MM-DD): ")
    df = df[(df['Data'] >= inicio) & (df['Data'] <= fim)]

# ========== RELATÓRIOS ==========
total_faturado = df['Faturamento'].sum()
media_diaria = df.groupby('Data')['Faturamento'].sum().mean()
top_produtos = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).head(3)
faturamento_produtos = df.groupby('Produto')['Faturamento'].sum().sort_values(ascending=False)
faturamento_diario = df.groupby('Data')['Faturamento'].sum()
dia_maior_faturamento = faturamento_diario.idxmax()

# ========== EXPORTAR RELATÓRIO TXT ==========
if EXPORTAR_RELATORIO_TXT:
    with open('relatorio_geral.txt', 'w', encoding='utf-8') as file:
        file.write("📊 RELATÓRIO DE VENDAS 📊\n\n")
        file.write(f"Total Faturado: R$ {total_faturado:.2f}\n")
        file.write(f"Média Diária de Faturamento: R$ {media_diaria:.2f}\n")
        file.write(f"Dia com maior faturamento: {dia_maior_faturamento.date()} (R$ {faturamento_diario.max():.2f})\n\n")
        file.write("Top 3 Produtos Mais Vendidos (em quantidade):\n")
        file.write(top_produtos.to_string())
        file.write("\n\nFaturamento por Produto:\n")
        file.write(faturamento_produtos.to_string())
    print("✅ Relatório exportado como 'relatorio_geral.txt'")

# ========== GRÁFICO DE BARRAS ==========
plt.figure(figsize=(10, 6))
barras = plt.bar(faturamento_produtos.index, faturamento_produtos.values, color='royalblue', edgecolor='black')
plt.title('Faturamento por Produto', fontsize=14, fontweight='bold')
plt.xlabel('Produto')
plt.ylabel('Faturamento (R$)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
for bar in barras:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 10, f'R$ {yval:.2f}', ha='center', fontsize=8)
plt.tight_layout()
if EXPORTAR_GRAFICOS:
    plt.savefig('grafico_barras.png', dpi=300)
plt.show()

# ========== GRÁFICO DE PIZZA ==========
plt.figure(figsize=(8, 8))
plt.pie(faturamento_produtos, labels=faturamento_produtos.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição do Faturamento por Produto')
if EXPORTAR_GRAFICOS:
    plt.savefig('grafico_pizza.png', dpi=300)
plt.show()

# ========== GRÁFICO DE LINHA ==========
plt.figure(figsize=(10, 5))
plt.plot(faturamento_diario.index, faturamento_diario.values, marker='o', linestyle='-', color='green')
plt.title('Faturamento ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Faturamento (R$)')
plt.grid(True)
plt.tight_layout()
if EXPORTAR_GRAFICOS:
    plt.savefig('grafico_linha.png', dpi=300)
plt.show()
