import pandas as pd
import numpy as np

df = pd.read_csv('D:/pro whitehat/PRO-C142-Project-Boilerplate-main/PRO-C142-Project-Boilerplate-main/articles.csv')

df = df.sort_values(['total_events'], ascending=[False])

output = df[["url", "title", "text", "lang", "total_events"]].head(20)