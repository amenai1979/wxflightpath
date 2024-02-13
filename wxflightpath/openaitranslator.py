import shelve
from functools import lru_cache

import openai
import requests
#from translate import Translator

from wxflightpath import config

import re




@lru_cache(maxsize=None)
def rapidtranslate(input="text to translate", lang='fr'):
    url = "https://text-translator2.p.rapidapi.com/translate"
    payload = {
        "source_language": "en",
        "target_language": lang,
        "text": fixup(input.upper())
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": config['SECURITY']['RAPIDAPI'],
        "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
    }
    response = requests.post(url, data=payload, headers=headers)
    return response.json()['data']['translatedText']


"""
@lru_cache(maxsize=None)
def mstranslate(input="text to translate", lang="fr"):
    translator = Translator(to_lang=lang)
    translation = translator.translate(fixup(input.upper()))
    return translation
"""

@lru_cache(maxsize=None)
def fixup(input="text"):
    output = input
    output = output.replace("WINDS", "Reported Surface Winds")
    output = output.replace("SKY CLEAR", "Reported Sky Conditions Clear")
    return output


# Set your OpenAI API key
openai.api_key = config['SECURITY']['OAI']


@lru_cache(maxsize=None)
def oaitranslate(input='text to translate', lang='fr'):
    # Define the text you want to translate
    # text_to_translate = "METAR LFRO 070600Z AUTO 02005KT 340V110 9999 BKN030 BKN035 BKN052 07/03 Q1024"
    # Specify the target language for translation
    if lang == 'fr':
        target_language = "français"
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": f"you are translating to {target_language}"},
                {"role": "user", "content": f"{input}"}],
            max_tokens=50,
            temperature=0.1,
            top_p=0.5,
            n=1,
            frequency_penalty=0.1,
            presence_penalty=0.1
        )
        # print(response.choices[0].message.content)
        # print(response.usage.total_tokens)
        return response.choices[0].message.content
    else:
        return input


@lru_cache(maxsize=None)
def translate(input="text to translate", lang='fr'):
    split_input=re.split(r'[.,-]|(\bbecoming\b)', input)
    split_input=[item.strip().lower() for item in split_input if item]
    #split_input = input.split('.')
    with shelve.open(config['DATA']['TRANSLATOR_DB']) as db:
        for x in split_input:
            if x not in db.keys():
                # db[x] = mstranslate(input=x)
                # db[x] = rapidtranslate(input=x)
                db[x] = oaitranslate(input=x)
        aggregated_translation = [db[x] for x in split_input]
    return ".".join(aggregated_translation)
