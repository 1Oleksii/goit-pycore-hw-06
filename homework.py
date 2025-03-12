import pandas as pd

url = "https://uk.wikipedia.org/wiki/Населення_України#Народжуваність"
tables = pd.read_html(url)

for i, table in enumerate(tables):
    print(f"Таблиця {i}:")
    print(table.head(), "\n")
