#transalated text to another language
from translate import Translator
    #use googletrans library to translate text
translator = Translator(from_lang="english", to_lang="spanish")
translation = translator.translate("this is a powerfull library")
print(translation)
