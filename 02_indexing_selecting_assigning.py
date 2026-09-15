# Kaggle Pandas — Indexing, Selecting & Assigning

# Conteúdo estudado:
# - Seleção de colunas
# - Seleção de linhas
# - Indexação com []
# - Seleção por posição com iloc
# - Seleção por rótulo com loc
# - Diferenças entre loc e iloc
# - Manipulação do índice com set_index()
# - Seleção condicional
# - Operadores & e |
# - Filtro com isin()
# - Verificação de valores nulos com isnull() e notnull()
# - Atribuição de valores em DataFrames

# Exercício 1
# Selecionar a coluna "description" do DataFrame reviews.

desc = reviews['description']


# Exercício 2
# Selecionar a primeira descrição do DataFrame reviews.

first_description = reviews['description'][0]
# or
first_description = reviews.description.iloc[0]

# Exercício 3
# Selecionar a primeira linha do DataFrame reviews.

first_row = reviews.iloc[0]

# Exercício 4
# Selecionar as primeiras 10 descrições do DataFrame reviews.

first_descriptions = reviews['description'].head(10)

# Exercício 5
# Selecionar as linhas com índices 1, 2, 3, 5 e 8 do DataFrame reviews.

sample_reviews = reviews.loc[[1,2,3,5,8]]

# Exercício 6
# Selecionar as linhas com índices 0, 1, 10 e 100 e as colunas 'country', 'province', 'region_1' e 'region_2' do DataFrame reviews.

df = reviews.loc[[0,1,10,100],['country','province','region_1','region_2']]

# Exercício 7
# Selecionar os primeiros 100 registros das colunas country e variety.

df = reviews.loc[0:99,['country','variety']]

# Exercício 8
# Selecionar as linhas onde a coluna 'country' é igual a 'Italy'.

italian_wines = reviews.loc[reviews.country == 'Italy']

# Exercício 9
# Selecionar as linhas onde a coluna 'points' é maior ou igual a 95 e a coluna 'country' é igual a 'Australia' ou 'New Zealand'.

top_oceania_wines = reviews.loc[
    (reviews.points >= 95) & 
    ((reviews.country == 'Australia') | (reviews.country == 'New Zealand'))]

