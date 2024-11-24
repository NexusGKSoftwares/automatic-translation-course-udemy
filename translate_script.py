from googletrans import Translator

translator = Translator()

text_to_translate = "Hello, how are you?"
translated = translator.translate(text_to_translate, src='en', dest='es')
print(translated.text)

