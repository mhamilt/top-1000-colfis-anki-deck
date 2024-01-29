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
		if True: substitute é [accento appunto] else è [accento grave]
	"""
	
	if any([word.endswith(f"{vowel}'") for vowel in ['a','e','i','o','u']]):
		accents = {'a': 'à', 'e': 'è', 'i': 'ì', 'o': 'ò', 'u': 'ù'}
		vowel = word[-2]
		
		if any([word.endswith(f"{x}'") for x in ["che", "ne", "se"]]):
			word = word[:-2] + 'é'
		else:
			word = word[:-2] + accents[vowel]
	
	return word

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
		colfis.iat[x, 4] = substitute_accents(colfis.iat[x, 4])
	
	colfis[["Forma","Freq","Cat.Gram"]].to_csv(filename, sep='\t', index=False)

def add_translations():
	"""
	"""
	pass

def main():
	colfis = pd.read_csv("Forme_inverso.tsv", sep='\t')
	filter_colfis_top_1000("top_1000_freq.tsv", colfis.sort_values('Freq', ascending=False))
	filter_colfis_top_1000("top_1000_rank.tsv", colfis.sort_values('Rango'))
	freq = pd.read_csv("top_1000_freq.tsv", sep='\t')
	rank = pd.read_csv("top_1000_rank.tsv", sep='\t')
	trans = pd.read_csv("top_1000_rank_notated.tsv", sep='\t')
	rank = rank[["Forma","Freq","Cat.Gram"]].rename(columns={"Forma": "italiano", "Freq": "freq",})
	rank['english'] = ["<TEXT>" for x in range(1000)]
	wiktionary = pd.read_csv("wiktionary_top_1000.tsv", sep='\t')
	wiktionary['english'] = ["<TEXT>" for x in range(wiktionary.shape[0])]
	wiktionary = wiktionary.rename(columns={"word": "italiano", "occurrences (ppm)": "freq", "lemma forms": 'lemma'})
	wiktionary = wiktionary[['english', 'italiano', 'freq', 'lemma']]

	freq = freq[["Forma","Freq","Cat.Gram"]].rename(columns={"Forma": "italiano", "Freq": "freq",})
	freq['english'] = ["<TEXT>" for x in range(1000)]

	for x in range(trans.shape[0]):
		if freq.at[x, "italiano"] == trans.at[x, "italiano"]:
			freq.at[x, "english"] = trans.at[x, "english"]
		else:
			for y in range(trans.shape[0]):
				if freq.at[x, "italiano"] == trans.at[y, "italiano"]:
					freq.at[x, "english"] = trans.at[y, "english"]
	
	for x in range(trans.shape[0]):
		if rank.at[x, "italiano"] == trans.at[x, "italiano"]:
			rank.at[x, "english"] = trans.at[x, "english"]
		else:
			for y in range(trans.shape[0]):
				if rank.at[x, "italiano"] == trans.at[y, "italiano"]:
					rank.at[x, "english"] = trans.at[y, "english"]
	
	for x in range(wiktionary.shape[0]):
		if wiktionary.at[x, "italiano"] == trans.at[x, "italiano"]:
			wiktionary.at[x, "english"] = trans.at[x, "english"]
		else:
			for y in range(trans.shape[0]):
				if wiktionary.at[x, "italiano"] == trans.at[y, "italiano"]:
					wiktionary.at[x, "english"] = trans.at[y, "english"]

	rank.to_csv("top_1000_rank.tsv", sep='\t', index=False)
	freq.to_csv("top_1000_freq.tsv", sep='\t', index=False)
	wiktionary.to_csv("top_1000_wiktionary.tsv", sep='\t', index=False)


if __name__ == "__main__":
	main()
