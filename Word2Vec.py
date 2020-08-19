import nltk
import pandas as pd 
import random
import ast
import re 
from nltk import RegexpTokenizer
from gensim.models import Word2Vec, KeyedVectors
from gensim.utils import simple_preprocess
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords

stopwords_port = set(stopwords.words('portuguese'))


noticias = pd.read_csv(r'Dados/Noticias_ibov.csv', index_col = 0)

# Transformando a coluna em uma lista
all_phrases_globo = noticias.frases_globo.dropna()
all_phrases_globo = all_phrases_globo.values.tolist()
all_phrases_folha = noticias.frases_folha.dropna()
all_phrases_folha = all_phrases_folha.values.tolist()
all_phrases = all_phrases_folha + all_phrases_globo

# Função para transformar all_phrases em uma lista de frases legíveis
def retorna_lista (phrases):
    all_words_phrases = []
    for day in phrases:
        all_words_phrases.append(ast.literal_eval(day))
    all_words_phrases = [item.lower() for sublist in all_words_phrases for item in sublist]
    return all_words_phrases

all_phrases = retorna_lista(all_phrases)
all_phrases_filtered = []

#Filtrando e tokenizando as palavras dentro de cada frase
for phrase in all_phrases:
    phrase = re.sub(r'\d', '', phrase)
    phrase = re.sub(r'[^\w]', ' ', phrase)
    all_phrases_token = (word_tokenize(phrase))
    # filtered_phrase = [w for w in all_phrases_token if not w in stopwords_port]
    # all_phrases_filtered.append(filtered_phrase)
    all_phrases_filtered.append(all_phrases_token)

print(all_phrases_filtered[:15])

# Criando e salvando modelo W2V das notícias
model50 = Word2Vec(all_phrases_filtered,size=50, window=5, workers=32, min_count=1, sg=1)
print(model50.most_similar('ibovespa'))
model50.save('word2vec_50_no_num.model')

model100 = Word2Vec(all_phrases_filtered,size=100, window=5, workers=32, min_count=1, sg=1)
print(model100.most_similar('ibovespa'))
model100.save('word2vec_100_no_num.model')

model300 = Word2Vec(all_phrases_filtered,size=300, window=5, workers=32, min_count=1, sg=1)
print(model300.most_similar('ibovespa'))
model300.save('word2vec_300_no_num.model')