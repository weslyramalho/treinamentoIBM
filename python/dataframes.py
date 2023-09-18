import pandas as pd

dicionario = {'Autores' : ['Rick Riordan', 'J.R.R Tolkien', 'Rabelo', 'Machado de Assis'],
              'Titulo': ['O Ladrão de Raios', 'A sociedade do Anel', 'Mar de Monstros', 'Memorias'],
              'Preço': [41.2, 35.7, 39.5, 40.5]}
df= pd.DataFrame(dicionario)

print(df)