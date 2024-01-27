import pandas as pd

colfis = pd.read_csv("Forme_inverso.tsv", sep='\t')
colfis = colfis.sort_values('Rango')
colfis = colfis[colfis['Cat.Gram'].apply(lambda x: 'K' not in x)]
colfis = colfis[colfis['Forma'].apply(lambda x: '-' not in x)]
colfis = colfis[colfis['Forma'].apply(lambda x: not x.isdigit())]
colfis.drop_duplicates(subset=['Forma'], keep='first').head(1000)[["Forma","Freq","Cat.Gram"]].to_csv("top_1000.tsv", sep='\t', index=False)