import pandas as pd


def gram_cat_acronym_to_long_name(cat_gram_str):
	"""
	Translate between CoLFIS Grammatical Category Acronym and long form
	
	Parola sintagmatica is stripped out
	"""
	cat_gram_dict = {"B":"Avverbio","E":"Nome proprio","I":"Interiezione","N":"Pronome","P":"Preposizione","S":"Sostantivo",
"V":"Verbo","X":"Lingua non ben identificata","@":"Parola sintagmatica","C":"Congiunzione","G":"Aggettivo","K":"Punteggiatura",
"NU":"Numerale", "R":"Articolo", "TC":"Tempo composto di un verbo", "VA":"Verbo ausiliare", "Z":"Simbolo"}

	cat_gram_str = cat_gram_str.replace('@','')
	long_form = '' 
	if "IN" in cat_gram_str:
		cat_gram_str = cat_gram_str.split()
		long_form = cat_gram_dict[cat_gram_str[0]] + ' in ' + cat_gram_dict[cat_gram_str[2]]
	else:
		long_form = cat_gram_dict[cat_gram_str]
	return long_form

def main():
	colfis = pd.read_csv("Forme_inverso.tsv", sep='\t')
	

	# colfis = colfis.sort_values('Freq', ascending=False)
	colfis = colfis.sort_values('Rango')
	colfis = colfis[colfis['Cat.Gram'].apply(lambda x: 'Z' not in x)]
	colfis = colfis[colfis['Cat.Gram'].apply(lambda x: 'E' not in x)]
	colfis = colfis[colfis['Cat.Gram'].apply(lambda x: 'K' not in x)]
	colfis = colfis[colfis['Forma'].apply(lambda x: '-' not in x)]
	colfis = colfis[colfis['Forma'].apply(lambda x: not x.isdigit())]
	colfis = colfis[colfis['Forma'].apply(lambda x: x not in ['poter', 'aver', 'far', 'andar', 'leader', 'pur', 'maggior'])]
	colfis = colfis.drop_duplicates(subset=['Forma'], keep='first').head(1000)
	
	for x in range(1000):		
		cat_gram = gram_cat_acronym_to_long_name(colfis.iat[x, 5])			
		colfis.iat[x, 5] = cat_gram
	# colfis.to_csv("top_1000_rank.tsv", sep='\t', index=False)
	colfis[["Forma","Freq","Cat.Gram"]].to_csv("top_1000.tsv", sep='\t', index=False)




if __name__ == "__main__":
	main()
