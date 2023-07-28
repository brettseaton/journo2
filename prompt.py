import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def inference(article_type, article):
    prompt = ""
    if article_type == "NYT":
        with open('prompts.txt') as f:
            contents = f.read()
            prompt = contents + article + "\nEdited:"
    # print(prompt)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )['choices'][0]['text']
    original_words = set(article.split())
    edited_words = response.split()
    result = []
    for word in edited_words:
        if word not in original_words:
            # The word is not in the original text, so it should be highlighted
            result.append((word, True, 'yellow'))  # Replace 'yellow' with your chosen color
        else:
            # The word is in the original text, so it shouldn't be highlighted
            result.append((word, False, ''))
    print(result)
    return result

