
import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados do arquivo CSV
df = pd.read_csv('gasolina.csv')

# Define o tamanho do gráfico
plt.figure(figsize=(10, 6))

# Plota o gráfico de linha com o dia no eixo x e o preço no eixo y
plt.plot(df['dia'], df['venda'])

# Define o título do gráfico e dos eixos
plt.title('Preço da Gasolina por Dia')
plt.xlabel('Dia')
plt.ylabel('Preço')

# Salva a imagem do gráfico em um arquivo PNG
plt.savefig('gasolina.png')
