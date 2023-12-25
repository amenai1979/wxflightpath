import logging
from gtts import gTTS
import os
from functools import lru_cache

@lru_cache(maxsize=None)
def renderaudio(title="briefing", input="text", lang='en'):
    filename=None
    assert input != (None or '')
    text_to_speak = input
    language = lang
    try:
        tts = gTTS(text=text_to_speak, lang=language, slow=False)
        filename = "../audio/" + title + ".mp3"
        tts.save(filename)
    except Exception as e:
        logging.error("Error rendering the audio briefing %s", e)
    return filename
    # For Linux or macOS, you can use something like 'xdg-open audio.mp3' or 'open audio.mp3'


if __name__ == '__main__':
    briefing = "this is a briefing for captain Hadock!"
    filename = renderaudio(input=briefing)
    # Windows
    # os.system("start " + filename)
    # MacOS
    os.system("afplay " + filename)
