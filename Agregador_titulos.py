import pandas as pd

arquivo_globo = r'Dados/Historico_de_materias.csv'
df_globo = pd.read_csv(arquivo_globo)

arquivo_folha = r'Dados/articles.csv'
df_folha = pd.read_csv(arquivo_folha)

globo_agrupado = df_globo.groupby('data')['titulo'].apply(lambda x: '. '.join(x)).reset_index()
folha_agrupado = df_folha.groupby('date')['title'].apply(lambda x: '. '.join(x)).reset_index()

globo_agrupado.to_csv(r'Dados/Noticias_globo_agrupado.csv', index=False)
folha_agrupado.to_csv(r'Dados/Noticias_folha_agrupado.csv', index=False)