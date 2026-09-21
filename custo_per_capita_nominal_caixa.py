import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker 

# Anos da série histórica 
years = list(range(2010, 2026)) 

# Custo per capita do Funcionário Médio (R$ mil / ano) 
per_capita_func = [ 111.2, 126.4, 139.1, 165.1, 184.8, 211.3, 
                    225.7, 256.9, 260.0, 266.9, 284.1, 299.3, 
                    298.4, 350.5, 352.0, 385.8 ] 

# Custo per capita da Alta Cúpula (R$ mil / ano) 
per_capita_cupula = [ 371.1, 410.1, 454.4, 805.9, 1178.9, 1388.8, 
                    1605.3, 1454.1, 1525.7, 1363.7, 1290.2, 1372.9, 
                    1696.0, 1365.6, 1896.9, 1927.1 ] 

# Definição de cores 
color_cupula = '#8B0000' # Vermelho Escuro 
color_func = '#1F4E78' # Azul Marinho 

# Criação da figura e eixo 
fig, ax = plt.subplots(figsize=(12, 7), dpi=300) 

# Plotagem das linhas 
ax.plot(years, per_capita_cupula, marker='o', linewidth=2.5, color=color_cupula, 
        label='Alta Cúpula (Pres, VPs, DIR, Conselhos & Comitês)', zorder=4) 
ax.plot(years, per_capita_func, marker='s', linewidth=2.5, color=color_func, 
        label='Funcionário Médio CAIXA', zorder=4) 

# Rótulos nos pontos - Alta Cúpula 
for x, y in zip(years, per_capita_cupula): 
    val_str = f"{int(round(y)):,}".replace(',', '.') 
    if x in [2010, 2025]: 
        ax.annotate(val_str, (x, y), textcoords="offset points", xytext=(0, 10), 
                    ha='center', fontweight='bold', color=color_cupula, fontsize=9, 
                    bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=color_cupula, lw=1)) 
    else: 
        ax.annotate(val_str, (x, y), textcoords="offset points", xytext=(0, 8), 
                    ha='center', color=color_cupula, fontsize=8) 

# Rótulos nos pontos - Funcionário Médio 
for x, y in zip(years, per_capita_func): 
    val_str = f"{int(round(y)):,}".replace(',', '.') 
    if x in [2010, 2025]: 
        ax.annotate(val_str, (x, y), textcoords="offset points", xytext=(0, -15), 
                    ha='center', fontweight='bold', color=color_func, fontsize=9, 
                    bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=color_func, lw=1)) 
    else: 
        ax.annotate(val_str, (x, y), textcoords="offset points", xytext=(0, -12), 
                    ha='center', color=color_func, fontsize=8) 

# Títulos e eixos 
ax.set_title('Evolução do Custo Per Capita Nominal: \n Alta Cúpula vs. Funcionário Médio CAIXA (2010–2025)', 
            fontsize=13, fontweight='bold', pad=5, color='#1A1A1A') 
ax.set_ylabel('Custo Per Capita (R$ mil / ano)', 
            fontsize=11, fontweight='bold', color='#333333') 
ax.set_xticks(years) 
ax.set_xticklabels([str(y) for y in years], fontsize=9.5, fontweight='bold') 
ax.set_ylim(0, 2200) 

# Formatação visual do gráfico 
ax.grid(True, linestyle='--', alpha=0.5, zorder=0) 
ax.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='#CCCCCC', fontsize=10.5) 
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f"{int(x):,}".replace(',', '.'))) 

# Ajuste da caixa de notas explicativas no rodapé 
pos = ax.get_position() 
notes_text = ( "Notas Explicativas:\n"
            "• Funcionário Médio: Custo total de pessoal (salários PCCS, encargos, Saúde CAIXA, FUNCEF e PLR dos bancários) dividido pelo quadro total de empregados ativos.\n"
            "• Alta Cúpula (Pessoal-Chave): Presidente, Vice-Presidentes, Conselhos (CA/CF) e Comitês (honorários, encargos e Remuneração Variável RVA/PLR) divididos pelo quórum (~25 a ~35 membros).\n"
            "• Fonte: Demonstrações Financeiras Consolidadas e Notas Explicativas da CAIXA de 2010 a 2025 (https://ri.caixa.gov.br/informacoes-financeiras/central-de-resultados/)." )
fig.text(pos.x0-0.06, 0.05, notes_text, fontstyle='italic', fontsize=8, color='#444444', 
        bbox=dict(boxstyle='square,pad=0.1', facecolor='#F5F5F5', edgecolor='#D0D0D0', linewidth=0.8), 
        transform=fig.transFigure, va='bottom', ha='left')

# Margens da figura 
plt.subplots_adjust(bottom=0.18, top=0.92, left=0.08, right=0.96) 

# Salvar arquivo 
plt.savefig('custo_per_capita_nominal_caixa.png', dpi=300) 
plt.close()