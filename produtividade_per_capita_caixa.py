import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 1. Séries temporais completas (2003 a 2025)
years = list(range(2003, 2026))

# Receita Operacional Per Capita (R$ mil / ano)
rec_operacional = [
    144.8, 182.2, 265.5, 321.9, 368.6, 404.9, 482.1, 582.2,
    684.2, 684.3, 792.1, 865.2, 865.1, 865.2, 865.2, 835.2,
    823.6, 792.6, 877.5, 991.8, 1044.3, 846.7, 904.7
]

# Receita de Serviços e Tarifas Per Capita (R$ mil / ano)
rec_servicos = [
    34.5, 40.4, 45.6, 52.9, 59.7, 71.1, 83.2, 117.1,
    139.0, 154.4, 169.2, 187.4, 213.1, 233.6, 266.4, 324.5,
    333.5, 301.4, 308.1, 329.6, 355.2, 319.3, 345.7
]

# Custo Médio de Pessoal Per Capita (R$ mil / ano)
custo_pessoal = [
    70.2, 81.4, 81.8, 86.4, 90.8, 98.0, 104.6, 111.2,
    126.4, 139.1, 165.1, 184.8, 211.2, 225.7, 256.8, 259.9,
    266.9, 284.1, 299.3, 339.5, 350.5, 352.0, 385.8
]

# Quadro de Empregados Concursados Ativos (em milhares)
quadro_mil = [
    57.4, 59.9, 68.3, 72.3, 78.4, 82.2, 85.3, 89.5,
    91.0, 92.5, 95.2, 98.2, 97.2, 93.2, 87.4, 83.2,
    81.0, 80.0, 77.6, 76.2, 72.0, 84.0, 80.5
]

# 2. Definição da paleta de cores institucional
color_rec_op = '#005CA9'    # Azul CAIXA
color_rec_serv = '#1E7E34'  # Verde Corporativo
color_custo = '#8B0000'     # Vermelho Escuro
color_bar = '#8295A5'       # Azul Acinzentado Neutro

# 3. Criação da figura com dois eixos integrados
fig, (ax1, ax2) = plt.subplots(
    nrows=2, ncols=1, figsize=(14, 9), dpi=300, sharex=True,
    gridspec_kw={'height_ratios': [2.5, 1.0], 'hspace': 0.18}
)

# -------------------------------------------------------------
# GRÁFICO SUPERIOR: Séries de Produtividade e Custo Per Capita
# -------------------------------------------------------------
ax1.plot(years, rec_operacional, marker='o', markersize=5.5, linewidth=2.3, 
         color=color_rec_op, label='Receita Operacional Total / Empregado', zorder=4)
ax1.plot(years, rec_servicos, marker='s', markersize=5, linewidth=2.2, 
         color=color_rec_serv, label='Receita de Serviços e Tarifas / Empregado', zorder=4)
ax1.plot(years, custo_pessoal, marker='^', markersize=5.5, linewidth=2.2, linestyle='--', 
         color=color_custo, label='Custo Médio de Pessoal / Empregado', zorder=4)

# Destaques numéricos com caixas estilizadas (Início, Picos e Fim)
# Ponto 2003 (Início)
ax1.annotate(f"R$ {rec_operacional[0]:.1f} mil\n(2003)", (2003, rec_operacional[0]), 
             xytext=(2003, rec_operacional[0] + 55), ha='center', fontsize=8, fontweight='bold',
             color=color_rec_op, bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=color_rec_op, lw=1))

# Ponto 2023 (Pico Histórico de Receita Operacional)
idx_2023 = years.index(2023)
ax1.annotate(f"Pico: R$ {rec_operacional[idx_2023]:.1f} mil\n(2023)", (2023, rec_operacional[idx_2023]), 
             xytext=(2021.7, rec_operacional[idx_2023] + 45), ha='center', fontsize=8, fontweight='bold',
             color=color_rec_op, bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=color_rec_op, lw=1),
             arrowprops=dict(arrowstyle="->", color=color_rec_op, lw=0.8))

# Ponto 2025 (Receita Operacional, Serviços e Custo)
ax1.annotate(f"R$ {rec_operacional[-1]:.1f} mil", (2025, rec_operacional[-1]), 
             xytext=(2025, rec_operacional[-1] + 35), ha='center', fontsize=8.5, fontweight='bold',
             color=color_rec_op, bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=color_rec_op, lw=1))
ax1.annotate(f"R$ {rec_servicos[-1]:.1f} mil", (2025, rec_servicos[-1]), 
             xytext=(2025, rec_servicos[-1] - 30), ha='center', fontsize=8, fontweight='bold',
             color=color_rec_serv, bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=color_rec_serv, lw=1))
ax1.annotate(f"R$ {custo_pessoal[-1]:.1f} mil", (2025, custo_pessoal[-1]), 
             xytext=(2025, custo_pessoal[-1] + 30), ha='center', fontsize=8, fontweight='bold',
             color=color_custo, bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=color_custo, lw=1))

ax1.set_title('Evolução da Produtividade e Custos Per Capita Nominal da CAIXA (2003–2025)\n'
              'Receita Operacional por Empregado Cresceu 6,2x no Período', 
              fontsize=12.5, fontweight='bold', pad=10, color='#1A1A1A')
ax1.set_ylabel('Valores Per Capita (R$ mil / empregado)', fontsize=10, fontweight='bold', color='#333333')
ax1.set_ylim(0, 1180)
ax1.grid(True, linestyle='--', alpha=0.45, zorder=0)
ax1.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='#D0D0D0', fontsize=9.5)
ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f"{int(x):,}".replace(',', '.')))

# -------------------------------------------------------------
# GRÁFICO INFERIOR: Evolução do Quadro de Concursados Ativos
# -------------------------------------------------------------
bars = ax2.bar(years, quadro_mil, color=color_bar, width=0.58, edgecolor='none', zorder=3)

# Identificação de marcos no quadro: Pico (2014) e Mínima recente (2023)
idx_pico = years.index(2014)
ax2.annotate(f"Pico: {quadro_mil[idx_pico]:.1f} mil\n(2014)", (2014, quadro_mil[idx_pico]), 
             xytext=(2014, quadro_mil[idx_pico] + 10), ha='center', fontsize=7.8, fontweight='bold',
             color='#222222', arrowprops=dict(arrowstyle="->", color='#333333', lw=0.8))

idx_min = years.index(2023)
ax2.annotate(f"Mínima: {quadro_mil[idx_min]:.1f} mil\n(2023)", (2023, quadro_mil[idx_min]), 
             xytext=(2023, quadro_mil[idx_min] - 25), ha='center', fontsize=7.8, fontweight='bold',
             color='#222222', arrowprops=dict(arrowstyle="->", color='#333333', lw=0.8))

ax2.set_title('Evolução do Quadro de Empregados Concursados da CAIXA (em milhares)', 
              fontsize=10.5, fontweight='bold', pad=6, color='#1A1A1A')
ax2.set_ylabel('Empregados (mil)', fontsize=9.5, fontweight='bold', color='#333333')
ax2.set_xlabel('Ano', fontsize=10, fontweight='bold', color='#333333')
ax2.set_xticks(years)
ax2.set_xticklabels([str(y) for y in years], fontsize=8.5, fontweight='bold')
ax2.set_ylim(0, 125)
ax2.grid(True, linestyle='--', alpha=0.45, zorder=0)
ax2.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f"{int(x):,}".replace(',', '.')))

# -------------------------------------------------------------
# NOTAS EXPLICATIVAS E METODOLOGIA NO RODAPÉ
# -------------------------------------------------------------
notes_text = (
    "Notas Explicativas e Metodologia:\n"
    "• Produtividade Per Capita: Receita Operacional Total consolidada (intermediação financeira, câmbio e serviços/tarifas) dividida pelo total de empregados concursados ativos do exercício.\n"
    "• Custo Médio de Pessoal: Despesas totais com pessoal (salários, encargos sociais, Saúde CAIXA, previdência complementar FUNCEF e PLR bancária) divididas pelos empregados ativos.\n"
    "• Quadro de Pessoal: Efetivo próprio oficial concursado apurado ao encerramento de cada ano fiscal (desconsidera estagiários, aprendizes e terceirizados de apoio operacional).\n"
    "• Fonte dos Dados: Demonstrações Financeiras Consolidadas (DRE/DVA), Relatórios da Administração e Balanços Sociais da CAIXA (2003 a 2025)."
)

pos = ax2.get_position()
fig.text(pos.x0, 0.02, notes_text, fontstyle='italic', fontsize=7.8, color='#333333',
         bbox=dict(boxstyle='square,pad=0.5', facecolor='#F5F5F5', edgecolor='#D0D0D0', linewidth=0.8),
         transform=fig.transFigure, va='bottom', ha='left')

# Ajuste fino das margens da figura
plt.subplots_adjust(bottom=0.17, top=0.93, left=0.065, right=0.96)

# Salvar e exportar
plt.savefig('produtividade_per_capita_caixa.png', dpi=300)
plt.close()