from textblob import TextBlob

# Create a TextBlob object
blob = TextBlob("Hello, how are you?")

# Translate text to Arabic
translated_blob = blob.translate(to='ar')

print(translated_blob)
