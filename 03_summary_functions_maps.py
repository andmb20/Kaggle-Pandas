# Kaggle Pandas — Summary Functions and Maps

# Conteúdo estudado:
# - Resumo estatístico com describe()
# - Cálculo de média com mean()
# - Identificação de valores únicos com unique()
# - Contagem de valores com value_counts()
# - Transformação de valores com map()
# - Transformação de linhas e colunas com apply()
# - Uso do parâmetro axis em apply()
# - Aplicação de funções lambda
# - Operações vetorizadas entre Series
# - Operações entre Series e valores escalares
# - Combinação de Series com operadores
# - Diferença entre operações vetorizadas, map() e apply()
# - Criação de novas representações a partir dos dados
# - Entendimento de que map() e apply() não alteram os dados originais

# Exercício 1
# Calcular a mediana da coluna points do DataFrame reviews.
median_points = reviews.points.median()

# Exercício 2
# Identificar os países únicos presentes na coluna country do DataFrame reviews.
countries = reviews.country.unique()

# Exercício 3
# Contar o número de vinhos por país.
reviews_per_country = reviews.country.value_counts()

# Exercício 4
# Centralizar os valores da coluna price subtraindo a média dos preços.
centered_price = reviews.price - reviews.price.mean()

# Exercício 5
# Identificar o vinho com o melhor custo-benefício (pontuação por preço).
bargain_wine = reviews.loc[(reviews.points / reviews.price).idxmax(), 'title']

# Exercício 6
# Contar o número de vinhos que contêm as palavras-chave 'tropical' e 'fruity' na descrição.
descriptor_counts = pd.Series([reviews.description.str.contains('tropical').sum(), reviews.description.str.contains('fruity').sum()], ['tropical', 'fruity'])

# Exercício 7
# Criar uma nova coluna com a classificação de estrelas com base em critérios específicos.
star_ratings = reviews.apply(
    lambda rows: 3 if rows.country == 'Canada' or rows.points >= 95
    else (2 if rows.points >=85 else 1)
, axis=1)
