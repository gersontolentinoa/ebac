
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega os dados do arquivo CSV
df = pd.read_csv('gasolina.csv')

# Define o estilo do gráfico utilizando o Seaborn
sns.set(style='whitegrid')

# Cria o gráfico de linha com o dia no eixo x e o preço no eixo y
plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df, marker='o')

# Adiciona rótulos nos pontos de dados
for i, row in df.iterrows():
    plt.text(row['dia'], row['venda'], str(row['venda']), ha='center', va='bottom')

# Define o título do gráfico e dos eixos
plt.title('Preço da Gasolina por Dia')
plt.xlabel('Dia')
plt.ylabel('Preço')

# Salva a imagem do gráfico em um arquivo PNG
plt.savefig('gasolina.png')
