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

def substitute_accents(word):
	"""
	if word ends with vowel that is not e [a, i, o, u] then ', substitute [à, ì, ò, ù]
	if word ends with e', check if [ne, se, -che]
		if True: subititue é else è 
	"""
	pass

def filter_colfis_top_1000(filename, colfis):
	"""
	
	"""
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
	
	colfis[["Forma","Freq","Cat.Gram"]].to_csv(filename, sep='\t', index=False)



def main():
	colfis = pd.read_csv("Forme_inverso.tsv", sep='\t')	
	filter_colfis_top_1000("top_1000_freq.tsv", colfis.sort_values('Freq', ascending=False))
	filter_colfis_top_1000("top_1000_rank.tsv", colfis.sort_values('Rango'))
	

if __name__ == "__main__":
	main()
