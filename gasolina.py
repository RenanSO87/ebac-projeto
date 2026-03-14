import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('gasolina.csv')

# Create the plot
plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df, marker='o', label='Preço da Gasolina')
plt.title('Preço Médio da Gasolina em São Paulo (Julho 2021)')
plt.xlabel('Dia do Mês')
plt.ylabel('Preço (R$)')
plt.grid(True)
plt.legend()

# Save the plot as a PNG file
plt.savefig('gasolina.png')

# plt.show() # Commented out to prevent plot from showing when script is run independently
