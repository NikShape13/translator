import googletrans
from googletrans import Translator

translator = Translator()
languages = googletrans.LANGUAGES

with open('text.txt', 'r', encoding='utf-8') as file:
    lines = [line.rstrip() for line in file]


def detect_language(text):
    detector = str(translator.detect(text)).split(',')[0].split('=')[1]
    return languages[detector].title()


def translate(text):
    language = detect_language(text)
    result = translator.translate(text, dest='ru')
    return (f"Translated from {language} : {result.text}")


for line in lines:
    result = translate(line)

    with open('result.txt', 'a', encoding='utf-8') as file:
        file.write(f"{result}\n")
