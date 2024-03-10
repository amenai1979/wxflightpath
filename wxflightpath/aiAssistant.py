import shelve
from functools import lru_cache
import openai
import requests
from wxflightpath import config
import re


openai.api_key = config['SECURITY']['OAI']

@lru_cache(maxsize=None)
def summarize(input='text to summarize'):
    response = openai.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": f"Summarize in a short set of sentences if IFR, Marginal VFR or VFR where IFR means visibility less than 3 km, fog  and or ceilings less than 500 feet, Marginal VFR means visibility less than 5 km and or cieling less than 1500 feet, VFR means the exact opposite of IFR and Marginal VFR. Also state the wind conditions. Warn if there are thudesrtorms, precipitation or reduced ceiling and visibility"},
                {"role": "user", "content": f"{input}"}],
            max_tokens=100,
            temperature=0.1,
            top_p=0.5,
            n=1,
            frequency_penalty=0.1,
            presence_penalty=0.1
        )
    return response.choices[0].message.content



if __name__=='__main__':
    print(summarize("Overcast layer at 500ft.  Winds one zero zero at 15 knots gusting to 25 knots"))
