import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("models/medical_qa.csv")

data = data.dropna()

questions = data["Question"].astype(str).tolist()
answers = data["Answer"].astype(str).tolist()

# Create TF-IDF model
vectorizer = TfidfVectorizer(stop_words="english")
question_vectors = vectorizer.fit_transform(questions)

st.set_page_config(page_title="Medical Q&A Chatbot", page_icon="🩺")

st.title("🩺 Medical Q&A Chatbot")
st.write("Ask any medical question.")

user_question = st.text_input("Enter your question:")

if st.button("Get Answer"):

    if user_question.strip() == "":
        st.warning("Please enter a question.")

    else:
        user_vector = vectorizer.transform([user_question])

        similarity = cosine_similarity(user_vector, question_vectors)

        best_index = similarity.argmax()

        score = similarity[0][best_index]

        if score < 0.10:
            st.error("I couldn't find an answer.")
        else:
            st.success(answers[best_index])