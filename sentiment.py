from textblob import TextBlob


def analyze_sentiment(text):

    text = text.lower()

    # Medical emotional words
    negative_words = [
        "scared",
        "afraid",
        "worried",
        "pain",
        "hurt",
        "sad",
        "anxious",
        "fear",
        "serious"
    ]

    positive_words = [
        "happy",
        "better",
        "good",
        "fine",
        "thanks",
        "thank you",
        "recovered"
    ]


    for word in negative_words:
        if word in text:
            return "Negative 😟"


    for word in positive_words:
        if word in text:
            return "Positive 😊"


    polarity = TextBlob(text).sentiment.polarity


    if polarity > 0:
        return "Positive 😊"

    elif polarity < 0:
        return "Negative 😟"

    else:
        return "Neutral 😐"


if __name__ == "__main__":
    print(analyze_sentiment(
        "I am scared because I have chest pain"
    ))