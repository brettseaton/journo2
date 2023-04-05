import os
import openai

openai.api_key = <API KEY>

def inference(article_type, article):
	prompt = ""
	if(article_type == "NYT"):
		with open('prompts.txt') as f:
		    contents = f.read()
		    prompt = contents + article + "\nEdited:"
	#print(prompt)
	response = openai.Completion.create(
	  model="text-davinci-003",
	  prompt= prompt,
	  temperature=0.5,
	  max_tokens=2000,
	  top_p=1,
	  frequency_penalty=0,
	  presence_penalty=0
	)['choices'][0]['text']
	print(response)
	return response
