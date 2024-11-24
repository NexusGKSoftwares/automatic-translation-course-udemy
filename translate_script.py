import time
import goslate

gs = goslate.Goslate()

text_to_translate = "Hello, how are you?"
target_language = 'es'

# Wait 1 second between requests
time.sleep(1)
translation = gs.translate(text_to_translate, target_language)
print(translation)
