#Classificar pacientes ortopedicos como normal ou abnormal usando machine learning
#Há 6 atributos biomecânimos que descrevem a postura da pelve e da coluna lombar
#Classificar em: Normal, hérnia de disco e espondiolistese
#Classificação binaria: normal ou abnormal(hernia de disco + espondiolistese agrupadas)
#Cada paciente possui 6 atributos númericos: Incidência pelvica, Angulo de lordose lombar, inclinação sacral, raio pelvico, grau de espondiolistese
#Calsse(target/label) indica se o paciente é Normal ou Adnormal
#os dados vêm do UCI Machine Learning Repository.

# Importa bibliotecas necessárias
import warnings   # Usada para controlar ou suprimir mensagens de aviso do Python
import requests   # Usada para fazer requisições HTTP (baixar arquivos da internet, por exemplo)
import zipfile    # Permite trabalhar com arquivos compactados no formato .zip
import io         # Fornece ferramentas para lidar com fluxos de dados (ex: arquivos em memória)

# Configura o warnings para ignorar avisos (não vai mostrar mensagens de warning na execução)
warnings.simplefilter('ignore')

# Importa bibliotecas adicionais
import pandas as pd       # Biblioteca poderosa para manipulação e análise de dados
from scipy.io import arff # Permite carregar arquivos no formato .arff (usado em datasets de machine learning, como do Weka)

#URL onde está o arquivo ZIP com o dataset "vertebral_column_data"
f_zip = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00212/vertebral_column_data.zip'

# Faz a requisição HTTP para baixar o arquivo ZIP da URL
# O parâmetro stream=True permite que o download seja feito em partes (streaming)
r = requests.get(f_zip, stream=True)

# Abre o arquivo ZIP diretamente da memória (sem precisar salvar em disco antes)
Vertebral_zip = zipfile.ZipFile(io.BytesIO(r.content))

# Extrai todos os arquivos contidos no ZIP para a pasta atual
Vertebral_zip.extractall()
#Carrega o arquivo .arff (um formato de dataset usado no Weka)
# A função retorna uma tupla: (dados, metadados)
data = arff.loadarff('column_2C_weka.arff')

# Converte a primeira parte da tupla (os dados) em um DataFrame do Pandas
# Assim, fica mais fácil manipular, analisar e visualizar os dados
df = pd.DataFrame(data[0])
df.head()

#Exploração dos dados
df.shape

df.columns

df.dtypes
# Decodifica a coluna de classe que está em bytes
df['class'] = df['class'].str.decode('utf-8')

# Mapeia as classes 'Normal' e 'Abnormal' para valores numéricos
# 'Normal' -> 0, 'Abnormal' -> 1
df['class_encoded'] = df['class'].map({'Normal': 0, 'Abnormal': 1})

# Mostra as primeiras 5 linhas com a nova coluna codificada
print(df.head())

# Mostra o tipo de dado da nova coluna
print(df.dtypes)