import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carregar os dados do arquivo gasolina.csv
df_gasolina = pd.read_csv('gasolina.csv')

# 2. Gerar o gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df_gasolina, marker='o')
plt.title('Preço Médio da Gasolina em São Paulo (Julho/2021)')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.grid(True)
plt.xticks(df_gasolina['dia'])

# 3. Salvar o gráfico no arquivo gasolina.png
plt.savefig('gasolina.png')

# Exibir o gráfico (opcional)
# plt.show()
