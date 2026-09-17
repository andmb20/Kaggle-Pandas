# Kaggle Pandas — Renaming and Combining

# Conteúdo estudado:
# - Renomeação de colunas e índices com rename()
# - Renomeação do eixo de linhas e colunas com rename_axis()
# - Alteração do índice com set_index()
# - Combinação de DataFrames com concat()
# - Combinação de DataFrames por índices com join()
# - Uso de lsuffix e rsuffix para diferenciar colunas com nomes iguais

# Exercício 1
# Renomear as colunas region_1 e region_2 para region e locale, respectivamente.
renamed = reviews.rename(columns={'region_1':'region', 'region_2':'locale'})

# Exercício 2
# Renomear o eixo de linhas para 'wines'.
reindexed = reviews.rename_axis('wines', axis='rows')

# Exercício 3
# Combinar os DataFrames gaming_products e movie_products.
combined_products = pd.concat([gaming_products, movie_products])

# Exercício 4
# Combinar os DataFrames powerlifting_meets e powerlifting_competitors por índice.
powerlifting_combined = powerlifting_meets.set_index('MeetID').join(powerlifting_competitors.set_index('MeetID'))
