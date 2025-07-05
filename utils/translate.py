import requests
import os

def translate_title(text):
    url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"
    querystring = {"langpair":"es|en","q":text}
    headers = {
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()["responseData"]["translatedText"]
