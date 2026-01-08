import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
print("Resumo dos dados:")
print(df.describe())

# Gráfico: Experiência x Salário

plt.scatter(df["experiencia_anos"], df['salario'])
plt.xlabel("Experiência (anos)")
plt.ylabel("Salário")
plt.title("Experiência x Salário")
plt.show()

plt.scatter(df["salario"], df["idade"])
plt.xlabel("Salário")
plt.ylabel("Idade")
plt.title("Salário x Idade")
plt.show()

plt.scatter(df["horas_semana"], df["avaliacao"])
plt.xlabel("Horas por semana")
plt.ylabel("Avaliação de desempenho")
plt.title("Horas trabalhadas x Avaliação")
plt.show()
