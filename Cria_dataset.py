import pandas as pd

noticias_globo = pd.read_csv(r'Dados/Noticias_globo_tokenizado.csv', index_col = 0)
noticias_folha = pd.read_csv(r'Dados/Noticias_folha_tokenizado.csv', index_col = 0)
dados_var_ibov = pd.read_csv(r'Dados/Variacao_ibovespa.csv', index_col = 0)
dados_ibov = pd.read_csv(r'Dados/Fechamento_ibovespa.csv', index_col = 0)

noticias_globo.index.names = ['Data']
noticias_folha.index.names = ['Data']

noticias_geral = pd.merge(noticias_folha, noticias_globo, left_index = True, right_index=True, how='outer', suffixes=('_folha', '_globo'))
noticias_geral.index.names = ['Data']
print(noticias_geral)

var_pos_neg = []
for variacao in dados_var_ibov.Variacao:
    var_pos_neg.append(1 if float(variacao) > 0 else 0)

dados_var_ibov['Binario'] = var_pos_neg
dados_ibov_completo = pd.merge(dados_ibov, dados_var_ibov, on = 'Date', how = 'outer')

dados_ibov_completo.index.names = ['Data']

noticias_ibov = pd.merge(noticias_geral, dados_ibov_completo, on = 'Data', how = 'outer')

noticias_geral.to_csv(r'Dados/Noticias_geral.csv', index = True)
dados_ibov_completo.to_csv(r'Dados/Dados_ibov_completo.csv', index = True)
noticias_ibov.to_csv(r'Dados/Noticias_ibov.csv', index = True)