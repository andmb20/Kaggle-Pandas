# Kaggle Pandas — Data Types and Missing Values

# Conteúdo estudado:
# - Identificação do tipo de dado de uma Series com dtype
# - Identificação dos tipos de dados de todas as colunas com dtypes
# - Conversão de tipos de dados com astype()
# - Identificação do tipo de dado do índice com index.dtype
# - Identificação de valores ausentes com isnull()
# - Identificação de valores não ausentes com notnull()
# - Seleção de registros com valores ausentes
# - Preenchimento de valores ausentes com fillna()
# - Substituição de valores com replace()
# - Diferença entre valores ausentes (NaN) e valores substituíveis

# Exercício 1
# Identificar o tipo de dado da coluna points do DataFrame reviews.
dtype = reviews.points.dtype

# Exercício 2
# Converter os valores da coluna points para o tipo string.
point_strings = reviews.points.astype('str')

# Exercício 3
# Contar a quantidade de valores ausentes na coluna price.
n_missing_prices = reviews.price.isnull().sum()

# Exercício 4
# Substituir valores ausentes de region_1 por "Unknown", contar a ocorrência de cada região e ordenar em ordem decrescente.
reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)

