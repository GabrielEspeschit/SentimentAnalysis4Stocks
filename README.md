# Algoritmo de Previsão do Mercado de Capitais Utilizando Análise De Sentimentos em Notícias Financeiras

Esse repositório armazena os códigos utilizados para o Trabalho de Conclusão de Curso de Engenharia Elétrica na Universidade Federal de Minas Gerais (UFMG), apresentado no dia 29/10/2020 pelo aluno Gabriel Espeschit. O trabalho teve a orientação do Professor Frederico Guimarães. Esse trabalho investiga a utilização de léxicos na análise de notícias e verifica como isso impacta na previsão dos dados do mercado financeiro.

## Resumo do Trabalho
O mercado de capitais é definido por muitos profissionais do setor como sendo objetivo e regido pela análise. No entanto, é impossível remover a parcialidade humana das atividades do mercado. Sendo assim, propôs-se investigar o impacto no desempenho de algoritmos de aprendizado de máquina na previsão do mercado financeiro quando se introduz a análise sentimental de notícias no modelo. Utilizando um léxico para língua portuguesa, obteve-se a polaridade de textos extraídos de um site popular de notícias. As médias diárias das polaridades das notícias foram calculadas e agrupadas  com uma série temporal contendo os preços de fechamento do índice Ibovespa daquele mesmo dia. Esse conjunto de dados multivariados foi utilizado para treinar  dois algoritmos de aprendizado de máquina. Os resultados alcançados foram comparados aos obtidos quando se utiliza somente os preços de fechamento para treinar o modelo. Em ambos os casos, observou-se que o uso de uma série temporal multivariada, contendo os preços de fechamento e a polaridade das notícias do dia, teve um desempenho superior ao uso somente de uma série contendo os preços de fechamento. Quando submetidos a uma estratégia de investimento simples, observou-se um desempenho semelhante para os dois tipos de dados nos dois algoritmos. Porém, quando comparados com uma estratégia de _buy and hold,_  ambos obtiveram  um desempenho vastamente superior. O estudo demonstra que o uso de algoritmos de aprendizado de máquina são uma forma eficiente para realizar a previsão do mercado financeiro e que a introdução de dados exógenos ao modelo pode melhorar ainda mais seu desempenho. Nesse estudo, a utilização da polaridade diária de notícias se provou uma das variáveis exógenas que pode ser utilizada para aprimorar a performance do algoritmo.

## Arquivos nesse Repositório
Nesse repositório encontram-se todos os arquivos de programação utilizados no trabalho, bem como o arquivo de dados finais usado (após o processamento léxico). Os arquivos contendo os dados 'crús' não foram carregados devido à limitações do GitHub à tamanho de arquivos. Além disso, nesse repositório temos o estudo completo submetido para UFMG.

## Referenciando o Trabalho
BiBTEX:
@misc{espeschit_2020, title={Algoritmo de Previsão do Mercado de Capitais Utilizando Análise de Sentimentos em Notícias Financeiras}, url={https://zenodo.org/record/4262815}, journal={Zenodo}, author={Espeschit, G. S.}, year={2020}, month={Nov}}
IEEE:
[1]Espeschit, G. S., “Algoritmo de Previsão do Mercado de Capitais Utilizando Análise de Sentimentos em Notícias Financeiras”, Zenodo, 2020.



# [EN] Stock Market Prediction Algorithm Utilizing Sentiment Analysis on Financial News
This repository stores the codes used for Universidade Fedral de Minas Gerais' (UFMG) Electrical Engineering End of Course Thesis Paper, presented on 10/29/2020 by Gabriel Espeschit. The work was supervised by Professor Frederico Guimarães. This work investigates the use of lexicons in the analysis of news and verifies how it impacts the forecast of financial market data.

## Abstract
Financial markets are defined as being objective and analysis oriented by many professionals in the field. However, it is impossible to remove human subjectivity from market analysis. For that reason, it was proposed to investigate the impact on the performance of machine learning algorithms in the forecast of the financial market when sentimental analysis of news was introduced to the model. Using a lexicon for the Portuguese language, the polarity of texts extracted from a popular news website was obtained. The daily averages of news polarities were calculated and grouped with a time series containing the closing prices of the Ibovespa index for the same day. This set of multivariate data was used to train two machine learning algorithms. The results achieved were compared to those obtained when using only closing prices to train the model. In both cases, it was observed that the use of a multivariate time series, containing the closing prices and the polarity of the daily news, outperformed the use of a series containing only the closing prices. When used in a simple investment strategy, a similar performance was observed for both types of data, in both algorithms. However, when compared to a buy and hold strategy, they achieved a vastly superior performance. The study shows that the use of machine learning algorithms is an efficient way to forecast the financial market and that the introduction of exogenous data to the model can further improve its performance. In this study, the use of daily news polarity proved to be one of the exogenous variables that can be used to improve the  algorithm’s performance.

## Files in This Repository
In this repository are all the programming files used in the work, as well as the final data file used (after the lexical processing). Files containing 'raw' data were not loaded due to GitHub's file size limitations. In addition, in this repository we have the complete study submitted to UFMG.

## Referencing the Paper
BiBTEX:
@misc{espeschit_2020, title={Algoritmo de Previsão do Mercado de Capitais Utilizando Análise de Sentimentos em Notícias Financeiras}, url={https://zenodo.org/record/4262815}, journal={Zenodo}, author={Espeschit, G. S.}, year={2020}, month={Nov}}
IEEE:
[1]Espeschit, G. S., “Algoritmo de Previsão do Mercado de Capitais Utilizando Análise de Sentimentos em Notícias Financeiras”, Zenodo, 2020.
