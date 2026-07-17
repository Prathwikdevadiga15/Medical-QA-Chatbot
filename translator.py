from deep_translator import GoogleTranslator

language_codes = {
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
    "Tamil": "ta"
}

def translate_text(text, language):

    if language == "English":
        return text

    try:
        return GoogleTranslator(
            source="auto",
            target=language_codes[language]
        ).translate(text)

    except Exception:
        return text