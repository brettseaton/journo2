import cohere
co = cohere.Client('Xg5MkHF053qIuEaMQlwojsf0SjvivIifXghgliJi')

def complete_sentence(input_sentence):
	word_count = len(input_sentence)
	prompt=f"This is a missing word-finding program. Given an incomplete sentence. The * words are replaced by the word you need to find. * = missing word. \n\nPrompt: I am calling in today to * a missing credit card. I lost my card when I was at the grocery store and I need to be sent a new one.\nCompleted Prompt: I am calling in today to report a missing credit card. I lost my card when I was at the grocery store and I need to be sent a new one.\n--\nPrompt: I work as a *. I repair wooden objects and structures.\nCorrect Prompt: I work as a carpenter. I repair wooden objects and structures.\n--\nPrompt: I was wondering if you had any time to jump on a quick call to * you do at Netflix and what the culture is like.\nCorrect Prompt: I was wondering if you had any time to jump on a quick call to share the work you do at Netflix and what the culture is like.\n--\nPrompt: Data augmentation is * when we don’t have representative data for all our targeted user personas. \nCompleted Prompt: Data augmentation is beneficial when we don’t have representative data for all our targeted user personas. \n--\nPrompt: Data augmentation is * when we don’t have representative data for all our targeted user personas. \nCompleted Prompt: Data augmentation is helpful when we don’t have representative data for all our targeted user personas. \n--\nPrompt: I\'d * to know if there are any internship opportunities in your team during the winter or summer.\nCompleted Prompt: I\'d love to know if there are any internship opportunities in your team during the winter or summer.\n--\nPrompt: The method of * output tokens is a key concept in text generation with language models.\nCompleted Prompt: The method of picking output tokens is a key concept in text generation with language models.\n__\nPrompt: I have a family of 4. My *, and 3 children.\nCompleted Prompt: I have a family of 4. My wife, and 3 children.\n--\nPrompt: The rough storm suddenly *.\nCompleted Prompt: The rough storm suddenly abated.\n--\nPrompt: {input_sentence}\nCompleted Prompt:"
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