import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
import string
from nltk import ngrams, Counter, FreqDist


# Pegando as stopwords (SW)
stop_words_port = stopwords.words('portuguese')
stop_words_en = stopwords.words('english')
ponctuation = RegexpTokenizer(r'\w+')
# Importando os arquivos
noticias = r'Dados/Arquivo/Noticias_globo_agrupado.csv'
df_noticias = pd.read_csv(noticias, index_col=0)
# Renomeando a coluna do dataframe
df_noticias.columns = ['titulo']

# Tokenizado as frases  de cada dia de noticias
# Para cada frase, também se tokeniza as palavras dessas frases com e sem SW
frases_noticias = df_noticias.titulo.apply(sent_tokenize)
palavras_noticias = df_noticias.titulo.apply(word_tokenize)
palavras_noticias_filtradas = df_noticias.titulo.apply(ponctuation.tokenize)
palavras_noticias_filtradas = palavras_noticias_filtradas.apply(lambda x: [item for item in x if item not in (stop_words_port)])

# Fazendo o Ngrams das palavras
bigram_palavras = palavras_noticias.apply(ngrams, n=2)
bigram_palavras_filtradas = palavras_noticias_filtradas.apply(ngrams, n=2) 
trigram_palavras = palavras_noticias.apply(ngrams, n=3)
trigram_palavras_filtradas = palavras_noticias_filtradas.apply(ngrams, n=3)

data = {
    'frases': frases_noticias,
    'palavras': palavras_noticias,
    'palavras_filtradas': palavras_noticias_filtradas,
    'bigram_palavas': bigram_palavras.apply(list),
    'bigram_filtrado': bigram_palavras_filtradas.apply(list),
    'trigram_palavras': trigram_palavras.apply(list),
    'trigram_filtrado': trigram_palavras_filtradas.apply(list)
}

# Transformando o dicionário em um dataframe com todos os dias de noticioas no periodo analisado
# Para dias sem noticias as colunas do DF ficam em NaN
df_noticias_tokenizado_temp = pd.DataFrame(data, index=df_noticias.index)
df_noticias_tokenizado_temp.index = pd.to_datetime(df_noticias_tokenizado_temp.index)
start_date = df_noticias_tokenizado_temp.index.min()
end_date = df_noticias_tokenizado_temp.index.max()
todos_dias = pd.date_range(start=start_date, end=end_date)
df_noticias_tokenizado = df_noticias_tokenizado_temp.reindex(todos_dias)
df_noticias_tokenizado.index.names = ['data']

print(df_noticias_tokenizado)
print(df_noticias_tokenizado_temp)
# print(df_noticias.head())

# Salvando o DF
# df_noticias_tokenizado.to_csv(r'Dados/Noticias_folha_tokenizado.csv')