import warnings
import requests
import zipfile
import io

# ignora mensagens de avisos para não poluir a saída do programa 
warnings.simplefilter('ignore')

import pandas as pd
# importa função para ler arquivos
from scipy.io import arff

# url do arquivo zip com o dataset "vertebral column" no repositório da UCI
f_zip = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00212/vertebral_column_data.zip'

# Faz o download do arquivo zip a partir da url
r = requests.get(f_zip, stream=True)

# converte o conteúdo baixado (r.content) em um arquivo de memória (bytesIO) e abre um arquivo zip para manipulação
Vertebral_zip = zipfile.ZipFile(io.BytesIO(r.content))

# Lista os arquivos dentro do zip para verificar o nome correto
print("Arquivos no ZIP:", Vertebral_zip.namelist())

# Extrair todos os arquivos do zip para o diretorio atual
Vertebral_zip.extractall()


data = arff.loadarff('column_2C.arff')


# cria o dataframe tabela do pandas com dados carregados
df = pd.DataFrame(data[0])

# mostra as 5 primeiras linhas 
print(df.head())

