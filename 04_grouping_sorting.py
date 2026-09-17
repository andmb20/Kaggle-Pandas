# Kaggle Pandas — Grouping and Sorting

# Conteúdo estudado:
# - Agrupamento de dados com groupby()
# - Análises por grupo
# - Funções de resumo em grupos
# - Uso do apply() em agrupamentos
# - Agregação de dados com agg()
# - Agrupamento por múltiplas colunas
# - MultiIndex
# - Conversão de MultiIndex com reset_index()
# - Ordenação por valores com sort_values()
# - Ordenação por índice com sort_index()
# - Ordenação por múltiplas colunas

# Exercício 1
# Contar o número de avaliações feitas por cada crítico, identificado pelo Twitter handle.
reviews_written = reviews.groupby('taster_twitter_handle').size()

# Exercício 2
# Encontrar a maior pontuação atribuída para cada preço de vinho.
best_rating_per_price = reviews.groupby('price').points.max()

# Exercício 3
# Encontrar os preços mínimo e máximo de cada variedade de vinho.
price_extremes = reviews.groupby('variety').price.aggregate(['min', 'max'])

# Exercício 4
# Ordenar as variedades de vinhos por preço mínimo e máximo.
sorted_varieties = price_extremes.copy().sort_values(
    by=['min' ,'max'],
    ascending=False
)

# Exercício 5
# Calcular a pontuação média de vinhos por crítico.
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

# Exercício 6
# Contar o número de vinhos por país e variedade.
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)
