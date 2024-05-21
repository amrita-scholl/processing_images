# processimages_module.py
import base64
import requests
import os
from dotenv import load_dotenv
load_dotenv()


def is_pdf_file(file_path):
    """
    Check if a file path has a .pdf extension.
    
    Args:
    - file_path (str): The path of the file.
    
    Returns:
    - bool: True if the file has a .pdf extension, False otherwise.
    """
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == '.pdf'

# OpenAI API Key
api_key = os.environ.get("OPENAI_API_KEY")

def process_images_from_pdf(image,query):
    
    #print("process_images_from_pdf")
    #print(image)

    # Getting the base64 string
    base64_image = encode_image_pdf(image)


    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4o",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": query
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    return response


def encode_image(image_path):
   with open(image_path, "rb") as image_file:
     return base64.b64encode(image_file.read()).decode('utf-8')
   
def encode_image_pdf(image):
     
     return base64.b64encode(image).decode('utf-8')
   
def process_images(image_path,query):
    
    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4o",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": query
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    return response

