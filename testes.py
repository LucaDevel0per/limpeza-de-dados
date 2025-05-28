import pandas as pd
from pathlib import Path

tabela = Path('dados/NBA_PLAYERS.csv')

df = pd.read_csv(tabela)

print(df.info())