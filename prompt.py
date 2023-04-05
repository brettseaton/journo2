import os
import openai

openai.api_key = "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"

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


def inf2(article_type, article):
	with open('sample_input.txt') as f:
		    waste = f.read()
	response = inference("NYT", waste)

	if(article_type == "NYT"):
		intro_highlight = ["Muhammad Ali, who died Friday, in Phoenix, at the age of seventy-four, was the most extraordinary American figure of his era, a self-invented character of such physical dominance, political defiance, global fame, and sheer originality that no novelist you might name would dare conceive him."]
		vocab_highlight = ["despised", "resided in an unassuming abode", "man of frustrated ambitions", "tiny", "trade blows"]
		tone_highlight = []
		audience_highlight = []
		
		with open('NY_edited.txt') as f:
		    original_text = f.read()
		text_parts = []
		is_highlighted = False
		for part in original_text.split('|'):
		    if part in intro_highlight:
		        text_parts.append((part, True, "yellow"))
		        is_highlighted = False
		    elif part in vocab_highlight:
		        text_parts.append((part, True, "purple"))
		        is_highlighted = False
		    elif part in tone_highlight:
		        text_parts.append((part, True, "blue"))
		        is_highlighted = False
		    elif part in audience_highlight:
		        text_parts.append((part, True, "green"))
		        is_highlighted = False
		    else:
		        text_parts.append((part, is_highlighted, "normal"))
		        is_highlighted = not is_highlighted
		return text_parts
	if(article_type == "SI"):
		intro_highlight = ["He was fast of fist and foot -- lip, too -- a champion who promised to shock the world and did."]
		vocab_highlight = ["legendary", "unique character", "changed his name", "criticized", "the legendary champion", "an unassuming abode",
							"veritable bastion", "unparalleled", "heinous acts", "self-assurance", "one of the greats"]
		tone_highlight = ["a larger-than-life warrior, a fearless rebel, a devout believer, a captivating speaker, a trailblazing advocate, a hilarious entertainer, a versatile actor, a graceful dancer, a nimble butterfly, and a relentless bee - a true titan of courage and conviction."]
		audience_highlight = ["Ali's remarkable self-assurance was there from the start, and even as a teen-ager, he showed uncommon skill. He was incredibly disciplined even then, waking at dawn and running through Chickasaw Park. As an aspiring fighter, he tore through Golden Gloves competitions, leading his mentor to say, “The truth is, the only thing Cassius is going to have to read is his I.R.S. form, and I’m willing to help him do it.”"]

		with open('SI_Edited.txt') as f:
		    original_text = f.read()
		text_parts = []
		is_highlighted = False
		for part in original_text.split('|'):
		    if part in intro_highlight:
		        text_parts.append((part, True, "yellow"))
		        is_highlighted = False
		    elif part in vocab_highlight:
		        text_parts.append((part, True, "purple"))
		        is_highlighted = False
		    elif part in tone_highlight:
		        text_parts.append((part, True, "blue"))
		        is_highlighted = False
		    elif part in audience_highlight:
		        text_parts.append((part, True, "green"))
		        is_highlighted = False
		    else:
		        text_parts.append((part, is_highlighted, "normal"))
		        is_highlighted = not is_highlighted
		return text_parts
	return []