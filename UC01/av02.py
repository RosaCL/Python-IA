import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Criando o DataFrame
dados_clientes = {
    'idade': [25, 32, 45, 28, 50, 35, 22, 40, 30, 55],
    'abriu_email': [1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
    'clicou_link': [1, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    'comprou': [1, 0, 0, 1, 0, 1, 0, 1, 0, 0]
}

df_click = pd.DataFrame(dados_clientes)

# Visualização dos dados
print("Dados completos dos clientes:")
print(df_click)
print("\nEstatísticas descritivas:")
print(df_click.describe())

# Análise visual
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
sns.boxplot(x='comprou', y='idade', data=df_click)
plt.title('Idade vs Comprou')

plt.subplot(1, 3, 2)
sns.countplot(x='abriu_email', hue='comprou', data=df_click)
plt.title('Abertura de Email vs Compra')

plt.subplot(1, 3, 3)
sns.countplot(x='clicou_link', hue='comprou', data=df_click)
plt.title('Clique no Link vs Compra')

plt.tight_layout()
plt.show()

# Preparação dos dados
X = df_click[['idade', 'abriu_email', 'clicou_link']]
y = df_click['comprou']

print("\nVariáveis independentes (X):")
print(X)
print("\nVariável dependente (y):")
print(y)

# Dividindo os dados (como temos poucos dados, usaremos 80% para treino)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando e treinando o modelo
modelo = DecisionTreeClassifier(max_depth=2, random_state=42)
modelo.fit(X_train, y_train)

# Fazendo previsões
y_pred = modelo.predict(X_test)

# Avaliando o modelo
print("\nAcurácia do modelo:", accuracy_score(y_test, y_pred))
print("\nImportância das features:")
for feature, importance in zip(X.columns, modelo.feature_importances_):
    print(f"{feature}: {importance:.2f}")

