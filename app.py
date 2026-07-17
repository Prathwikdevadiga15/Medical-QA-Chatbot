import streamlit as st

from chatbot import get_answer
from entity_recognition import recognize_entities
from sentiment import analyze_sentiment


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Medical Q&A Chatbot",
    page_icon="🩺",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------
st.title("🩺 Medical Q&A Chatbot")

st.write(
    "AI-powered medical assistant with "
    "Question Answering, Entity Recognition, and Sentiment Analysis."
)

st.markdown("---")


# -----------------------------
# User Input
# -----------------------------
user_question = st.text_input(
    "Enter your medical question:"
)


# -----------------------------
# Main Processing
# -----------------------------
if user_question:

    # =============================
    # 1. Sentiment Analysis
    # =============================

    sentiment = analyze_sentiment(user_question)

    st.subheader("😊 Sentiment Analysis")
    st.write("Sentiment:", sentiment)


    if "Negative" in sentiment:
        st.warning(
            "I'm sorry you are feeling this way. "
            "I will try my best to help you."
        )

    elif "Positive" in sentiment:
        st.success(
            "I'm glad you are feeling positive!"
        )

    else:
        st.info(
            "Let's find information about your medical question."
        )


    # =============================
    # 2. Medical Entity Recognition
    # =============================

    entities = recognize_entities(user_question)

    st.subheader("🔍 Medical Entities Identified")

    entity_found = False


    if entities["Diseases"]:
        entity_found = True
        st.write("🦠 **Disease:**")

        for disease in entities["Diseases"]:
            st.write("•", disease)


    if entities["Symptoms"]:
        entity_found = True
        st.write("🤒 **Symptoms:**")

        for symptom in entities["Symptoms"]:
            st.write("•", symptom)


    if entities["Medicines"]:
        entity_found = True
        st.write("💊 **Medicines:**")

        for medicine in entities["Medicines"]:
            st.write("•", medicine)


    if entities["Treatments"]:
        entity_found = True
        st.write("🏥 **Treatments:**")

        for treatment in entities["Treatments"]:
            st.write("•", treatment)


    if not entity_found:
        st.info("No medical entities identified.")



    # =============================
    # 3. Medical Question Answer
    # =============================

    st.subheader("💬 Medical Answer")

    answer = get_answer(user_question)

    st.write(answer)



# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption(
    "Medical Q&A Chatbot | "
    "TF-IDF Retrieval | "
    "Cosine Similarity | "
    "Medical Entity Recognition | "
    "Sentiment Analysis"
)