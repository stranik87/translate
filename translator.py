from deep_translator import GoogleTranslator

def tarjimon(text):
    tarjima = GoogleTranslator(source='auto', target='en').translate(text)

    return tarjima