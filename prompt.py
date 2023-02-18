import cohere
co = cohere.Client('Xg5MkHF053qIuEaMQlwojsf0SjvivIifXghgliJi')



def complete_sentence(input_sentence):
	word_count = len(input_sentence)
	
	text_file = open("prompts.txt", "r")
	prompt = text_file.read()

	text_file.close()
	while(True):
		response = co.generate(
			model='xlarge',
			prompt=prompt,
			max_tokens=word_count*2,
			temperature=0.7,
			k=0,
			p=1,
			frequency_penalty=0,
			presence_penalty=0,
			stop_sequences=["--"],
			return_likelihoods='NONE')
		text = response.generations[0].text
		if(text.find('--') != -1):
			return text[0:text.index('--')]
	return "Try Again"

input_sentence = 'Whether you\'re looking to * a local museum or sample the city\'s varied cuisine, there is plenty to fill any itinerary.'

print(complete_sentence(input_sentence))
