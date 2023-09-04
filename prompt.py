# import os
# import openai
# import difflib
# from google.cloud import secretmanager
# from google.cloud import storage

# def get_file_from_gcs(bucket_name, blob_name):
#     storage_client = storage.Client()
#     bucket = storage_client.bucket(bucket_name)
#     blob = bucket.blob(blob_name)
#     return blob.download_as_text()

# # from dotenv import load_dotenv  # You don't need this anymore

# # load_dotenv()  # You don't need this anymore

# # Function to access secret from Secret Manager
# def access_secret_version(project_id, secret_id, version_id):
#     """
#     Access the payload for a given secret version.

#     The version can be a version number as a string (e.g. "5") or an
#     alias (e.g. "latest").
#     """

#     client = secretmanager.SecretManagerServiceClient()

#     # Build the resource name of the secret version
#     name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

#     # Access the secret version
#     response = client.access_secret_version(request={"name": name})

#     # Return the decoded payload
#     return response.payload.data.decode('UTF-8')


# def inference(article_type, article):
#     openai.api_key = access_secret_version('journo-396520', 'OPENAI_API_KEY', 'latest')
#     prompt = ""
    
#     # Define the bucket name
#     bucket_name = "journo-text-data"
    
#     if article_type == "NYT":
#         contents = get_file_from_gcs(bucket_name, 'prompts.txt')
#         prompt = contents + article + "\nEdited:"
#     elif article_type == "Mercury":
#         contents = get_file_from_gcs(bucket_name, 'mercuryprompts.txt')
#         prompt = contents + article + "\nEdited:"
#     elif article_type == "Sentinel":
#         contents = get_file_from_gcs(bucket_name, 'sentinelprompts.txt')
#         prompt = contents + article + "\nEdited:"
#     elif article_type == "Press":
#         contents = get_file_from_gcs(bucket_name, 'sheridanprompts.txt')
#         prompt = contents + article + "\nEdited:"
# 	# print(prompt)
# 	response = openai.Completion.create(
# 		model="text-davinci-003",
# 		prompt=prompt,
# 		temperature=0.4,
# 		max_tokens=2000,
# 		top_p=1,
# 		frequency_penalty=0,
# 		presence_penalty=0
# 	)['choices'][0]['text']
# 	matcher = difflib.SequenceMatcher(None, article.split(), response.split())
# 	ranges = []
# 	for tag, i1, i2, j1, j2 in matcher.get_opcodes():
# 		if tag == 'equal':
# 			ranges.append((j1, j2 - 1))
# 	result = []
# 	for index, word in enumerate(response.split()):
# 		samechecker = 0
# 		for start, end in ranges:
# 			if start <= index <= end:
# 				result.append((word, False, ''))
# 				samechecker = 1
# 				break
# 		if samechecker == 0:
# 			result.append((word, True, 'yellow'))				
# 	print(result)
# 	return result
import os
import openai
import difflib
from google.cloud import secretmanager
from google.cloud import storage

def get_file_from_gcs(bucket_name, blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    return blob.download_as_text()

# Function to access secret from Secret Manager
def access_secret_version(project_id, secret_id, version_id):
    """
    Access the payload for a given secret version.

    The version can be a version number as a string (e.g. "5") or an
    alias (e.g. "latest").
    """

    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version
    response = client.access_secret_version(request={"name": name})

    # Return the decoded payload
    return response.payload.data.decode('UTF-8')


def inference(article_type, article):
    openai.api_key = access_secret_version('journo-396520', 'OPENAI_API_KEY', 'latest')
    prompt = ""
    
    # Define the bucket name
    bucket_name = "journo-text-data"
    
    if article_type == "NYT":
        contents = get_file_from_gcs(bucket_name, 'prompts.txt')
        prompt = contents + article + "\nEdited:"
    elif article_type == "Mercury":
        contents = get_file_from_gcs(bucket_name, 'mercuryprompts.txt')
        prompt = contents + article + "\nEdited:"
    elif article_type == "Sentinel":
        contents = get_file_from_gcs(bucket_name, 'sentinelprompts.txt')
        prompt = contents + article + "\nEdited:"
    elif article_type == "Press":
        contents = get_file_from_gcs(bucket_name, 'sheridanprompts.txt')
        prompt = contents + article + "\nEdited:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.4,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )['choices'][0]['text']
    matcher = difflib.SequenceMatcher(None, article.split(), response.split())
    ranges = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            ranges.append((j1, j2 - 1))
    result = []
    for index, word in enumerate(response.split()):
        samechecker = 0
        for start, end in ranges:
            if start <= index <= end:
                result.append((word, False, ''))
                samechecker = 1
                break
        if samechecker == 0:
            result.append((word, True, 'yellow'))                
    print(result)
    return result


