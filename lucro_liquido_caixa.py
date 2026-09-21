import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Anos da série histórica (2003 a 2025)
years = list(range(2003, 2026))

# Lucro Líquido Anual Consolidado da CAIXA (R$ bilhões)
lucro_liquido = [
    1.62, 1.42, 2.07, 2.39, 2.39, 3.88, 3.00, 
    5.18, 5.18, 6.07, 6.72, 7.09, 7.16, 4.14, 
    12.52, 10.36, 21.06, 13.17, 17.27, 10.34, 11.73, 13.53, 13.16
]

# Definição de cores
color_main = '#005CA9'      # Azul CAIXA
color_highlight = '#8B0000' # Vermelho Carmesim para o pico

# Criação da figura e eixo
fig, ax = plt.subplots(figsize=(12, 7), dpi=300)

# Plotagem da linha e área de preenchimento
ax.plot(years, lucro_liquido, marker='o', markersize=6, linewidth=2.5, 
        color=color_main, label='Lucro Líquido Consolidado (R$ bi)', zorder=4)
ax.fill_between(years, lucro_liquido, alpha=0.08, color=color_main, zorder=3)

# Rótulos de valores nos pontos chave
for x, y in zip(years, lucro_liquido):
    # Destaques especiais: Início (2003), Recessão/PECLD (2016), Pico Histórico (2019) e Atual (2025)
    if x == 2019:
        ax.annotate(f"R$ {y:.2f} bi\n(Pico Recorde)", (x, y), textcoords="offset points", xytext=(0, 12), 
                    ha='center', fontweight='bold', color=color_highlight, fontsize=9.5, 
                    bbox=dict(boxstyle="round,pad=0.25", fc="#FFF0F0", ec=color_highlight, lw=1.2))
    elif x in [2003, 2019, 2025]:
        val_str = f"R$ {y:.2f} bi".replace('.', ',')
        ax.annotate(val_str, (x, y), textcoords="offset points", xytext=(0, 12), 
                    ha='center', fontweight='bold', color='#003366', fontsize=9, 
                    bbox=dict(boxstyle="round,pad=0.2", fc="#E6F0FA", ec=color_main, lw=1.0))
    else:
        val_str = f"{y:.1f}".replace('.', ',')
        ax.annotate(val_str, (x, y), textcoords="offset points", xytext=(0, 7), 
                    ha='center', color='#444444', fontsize=8)

# Títulos e eixos
ax.set_title('Evolução do Lucro Líquido Anual Consolidado da CAIXA (2003–2025)', 
             fontsize=13, fontweight='bold', pad=15, color='#1A1A1A')
ax.set_ylabel('Lucro Líquido Consolidado (R$ bilhões)', fontsize=11, fontweight='bold', color='#333333')
ax.set_xticks(years)
ax.set_xticklabels([str(y) for y in years], fontsize=8.5, rotation=45, fontweight='bold')
ax.set_ylim(0, 24)

# Formatação de grade e legenda
ax.grid(True, linestyle='--', alpha=0.5, zorder=0)
ax.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='#CCCCCC', fontsize=10)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f"R$ {int(x)} bi"))

# Caixa de notas explicativas e metodologia no rodapé
pos = ax.get_position()
notes_text = (
    "Notas Explicativas e Metodologia:\n"
    "• Lucro Líquido Consolidado: Resultado líquido auditado atribuível ao Conglomerado CAIXA ao encerramento de cada exercício financeiro.\n"
    "• Eventos Marcantes: O pico de 2019 (R$ 21,06 bi) reflete operações não recorrentes e alienações de participações/ativos (ex: IPO da Caixa Seguridade);\n"
    "  em 2016, o resultado reflete o reforço no provisionamento para devedores duvidosos (PECLD) durante a recessão econômica.\n"
    "• Fonte: Demonstrações Financeiras Consolidadas do 4º Trimestre da CAIXA (2003–2025)."
)

fig.text(pos.x0, 0.02, notes_text, fontstyle='italic', fontsize=8, color='#444444',
         bbox=dict(boxstyle='square,pad=0.6', facecolor='#F5F5F5', edgecolor='#D0D0D0', linewidth=0.8),
         transform=fig.transFigure, va='bottom', ha='left')

# Ajuste fino das margens da figura
plt.subplots_adjust(bottom=0.22, top=0.92, left=0.08, right=0.96)

# Salvar a imagem
plt.savefig('lucro_liquido_consolidado_caixa.png', dpi=300)
plt.close()