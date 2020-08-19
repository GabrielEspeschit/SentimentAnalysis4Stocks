from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd


# Adquirindo data de inicio e fim do dataset
df_globo_token = pd.read_csv(r'Dados/Noticias_globo_tokenizado.csv', index_col = 0)
df_folha_token = pd.read_csv(r'Dados/Noticias_folha_tokenizado.csv', index_col = 0)
start_date = min(df_globo_token.index.min(), df_folha_token.index.min())
end_date = max(df_globo_token.index.max(), df_folha_token.index.max())

# Pegando os valores correspondentes para o ibovespa
ibov_data = data.DataReader('^BVSP', 'yahoo', start_date, end_date)

# Transformando os dados do ibov em dataframes de variação e fechamento para analise
# Formula da variação: (fechamento(t)-fechamento(t-1))/fechamento(t-1)

fechamento = pd.DataFrame(index = ibov_data.index)
variacao_fechamento = pd.DataFrame(index = ibov_data.index)
fechamento['Fechamento'] = ibov_data['Close']
variacao_fechamento['Variacao'] = (fechamento - fechamento.shift(1))/(fechamento.shift(1))*100

variacao_fechamento.to_csv(r'Dados/Variacao_ibovespa.csv', index=True)
fechamento.to_csv(r'Dados/Fechamento_ibovespa.csv', index=True)