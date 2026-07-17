import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("models/medical_qa.csv")
data = data.dropna()

questions = data["Question"].astype(str).tolist()
answers = data["Answer"].astype(str).tolist()

# Create TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words="english")
question_vectors = vectorizer.fit_transform(questions)


def get_answer(user_question):
    """Return the best answer for the user's medical question."""

    user_vector = vectorizer.transform([user_question])
    similarity = cosine_similarity(user_vector, question_vectors)

    best_index = similarity.argmax()
    best_score = similarity[0][best_index]

    if best_score < 0.10:
        return "I couldn't find an answer."

    return answers[best_index]


# Run only if chatbot.py is executed directly
if __name__ == "__main__":

    print("=" * 50)
    print("      Medical Q&A Chatbot")
    print("=" * 50)
    print("Type 'exit' to quit.\n")

    while True:

        user_question = input("You: ")

        if user_question.lower() == "exit":
            print("Bot: Thank you! Stay healthy.")
            break

        print("Bot:", get_answer(user_question))