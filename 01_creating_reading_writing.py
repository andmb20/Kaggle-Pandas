# Kaggle Pandas — Creating, Reading and Writing

# Conteúdo estudado:
# - Criação de DataFrames
# - Criação de Series
# - Índices
# - Leitura de arquivos CSV
# - Uso do read_csv()
# - Uso do index_col
# - Uso do to_csv()

# Exercícios realizados no Kaggle:
# 1. Criar um DataFrame simples
# 2. Criar um DataFrame com índice personalizado
# 3. Criar uma Series
# 4. Ler um arquivo CSV
# 5. Salvar um DataFrame em um arquivo CSV


# Exercício 1
# Criar um DataFrame contendo Apples e Bananas.

import pandas as pd

fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})

print(fruits)


# Exercício 2
# Criar um DataFrame com vendas de frutas para 2017 e 2018, utilizando os anos como índice.

fruit_sales = pd.DataFrame(
    {'Apples': [35, 41], 'Bananas': [21, 34]},
    index=['2017 Sales', '2018 Sales']
)

print(fruit_sales)


# Exercício 3
# Criar uma Series contendo ingredientes, suas quantidades e o nome "Dinner".

ingredients = pd.Series(
    ['4 cups', '1 cup', '2 large', '1 can'],
    index=['Flour', 'Milk', 'Eggs', 'Spam'],
    name='Dinner'
)

print(ingredients)


# Exercício 4
# Ler o arquivo CSV de avaliações de vinhos utilizando a primeira coluna como índice.

reviews = pd.read_csv(
    '../input/wine-reviews/winemag-data_first150k.csv',
    index_col=0
)

print(reviews.head())


# Exercício 5

animals = pd.DataFrame(
    {'Cows': [12, 20], 'Goats': [22, 19]},
    index=['Year 1', 'Year 2']
)

# Salvar o DataFrame animals em um arquivo CSV com o nome cows_and_goats.csv.

animals.to_csv('cows_and_goats.csv')


