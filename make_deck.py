import pandas as pd
import os 
import genanki

def make_deck(corpus, deck_name, deck_filename, guid):
	my_model = genanki.Model(
	3745207544,
	'Simple Model',
	fields=[
		{'name': 'Italiano'},
		{'name': 'English'},
		{'name': 'Pronunciation'}, # ADD THIS
	],
	templates=[
		{
		'name': 'Card 1',
		'qfmt': '{{Italiano}}<br>{{Pronunciation}}',
		'afmt': '{{FrontSide}}<hr id="answer">{{English}}',
		},
	])

	my_deck = genanki.Deck(
	guid,
	deck_name)
	my_package = genanki.Package(my_deck)
	my_package.media_files = []

	
	for x in range(corpus.shape[0]):
		english = corpus.loc[x,'english']
		italian = corpus.loc[x,'italiano']
		filename = italian.replace("'", "-").replace(" ", "_") + ".mp3"
		my_note = genanki.Note(model=my_model, 
						 	   fields=[italian, 
									   english, 
									   f'[sound:{filename}]'])
		my_package.media_files.append(f'mp3/{filename}')
		my_deck.add_note(my_note)

	
	# my_package.media_files = [f'mp3/{wav}' for wav in os.listdir('mp3')]
	my_package.write_to_file(f'{deck_filename}.apkg')

def make_pronunciation_file(word):	
	filename = word.replace("'", "-").replace(" ", "_")
	command = f"say -r 160 -v 'Emma' --file-format=WAVE --data-format=alaw -o 'audio/{filename}.wav' \"{word}\""
	os.system(command)
	command = f"ffmpeg -i audio/{filename}.wav -vn -ar 44100 -ac 2 -b:a 96k mp3/{filename}.mp3"
	os.system(command)

def main():
	"""
	- concatenate each deck
	- remove duplicate italian words
	- send each word to 'say' command and output aiff
		say -v 'Emma' -o "audio/${word}.aiff" "${word}" 
	"""	
	freq = pd.read_csv("tsv/top_1000_freq.tsv", sep='\t')
	rank = pd.read_csv("tsv/top_1000_rank.tsv", sep='\t')
	wiki = pd.read_csv("tsv/top_1000_wiktionary.tsv", sep='\t')
	corpus = pd.concat([freq[['italiano']], 
						wiki[['italiano']],
						rank[['italiano']]]).drop_duplicates(subset=['italiano'], keep='first')
	
	for x in range(corpus.shape[0]):	
		word = corpus.iloc[x, 0]
		print(word, x, "out of", corpus.shape[0])
		make_pronunciation_file(word)
	
	make_deck(freq, "Top 1000 Italian words by CoLFIS Freq", "freq_italian", 1901898207)
	make_deck(freq, "Top 1000 Italian words by CoLFIS Rank", "rank_italian", 1508820474)	
	make_deck(freq, "Wiktionary Top '1000' Italian Words", "wiki_italian", 4206775067)


if __name__ == "__main__":
	main()	
