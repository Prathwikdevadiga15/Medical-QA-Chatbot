import streamlit as st

from chatbot import get_answer
from entity_recognition import recognize_entities
from sentiment import analyze_sentiment
from research_chatbot import search_paper
from image_analyzer import analyze_image
from translator import translate_text


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Medical & Research Assistant",
    page_icon="🤖",
    layout="centered"
)


st.title("🤖 AI Medical & Research Assistant")

st.write(
    "Medical Q&A | Research Assistant | Multimodal AI | Multilingual Support"
)


# -----------------------------
# Sidebar
# -----------------------------
assistant = st.sidebar.selectbox(
    "Choose Assistant",
    [
        "🩺 Medical Assistant",
        "📚 Research Assistant",
        "🖼️ Multimodal Assistant"
    ]
)


language = st.sidebar.selectbox(
    "🌍 Select Language",
    [
        "English",
        "Hindi",
        "Kannada",
        "Tamil"
    ]
)


# ============================================================
# MULTIMODAL ASSISTANT
# ============================================================

if assistant == "🖼️ Multimodal Assistant":

    st.subheader("🖼️ Multimodal AI Assistant")

    uploaded_file = st.file_uploader(
        "Upload an Image",
        type=["png", "jpg", "jpeg"]
    )


    question = st.text_input(
        "Ask a question about the image"
    )


    if uploaded_file:

        st.image(
            uploaded_file,
            caption="Uploaded Image",
            use_container_width=True
        )


    if st.button("Analyze Image"):

        result = analyze_image(
            uploaded_file,
            question
        )

        translated_result = translate_text(
            result,
            language
        )

        st.success(translated_result)



# ============================================================
# RESEARCH ASSISTANT
# ============================================================

elif assistant == "📚 Research Assistant":

    st.subheader("📚 Domain Expert Research Assistant")


    user_question = st.text_input(
        "Enter your research question:"
    )


    if user_question:


        result = search_paper(
            user_question
        )


        translated_result = translate_text(
            result,
            language
        )


        st.write(
            translated_result
        )



# ============================================================
# MEDICAL ASSISTANT
# ============================================================

else:


    st.subheader("🩺 Medical Q&A Assistant")


    user_question = st.text_input(
        "Enter your medical question:"
    )


    if user_question:


        # -----------------------------
        # Sentiment Analysis
        # -----------------------------

        sentiment = analyze_sentiment(
            user_question
        )


        st.subheader(
            "😊 Sentiment Analysis"
        )


        st.write(
            translate_text(
                sentiment,
                language
            )
        )


        if "Negative" in sentiment:

            st.warning(
                "I'm sorry you are feeling worried. I will try my best to help."
            )


        elif "Positive" in sentiment:

            st.success(
                "Glad to hear you are feeling positive!"
            )


        else:

            st.info(
                "Let's understand your medical question."
            )



        # -----------------------------
        # Entity Recognition
        # -----------------------------

        entities = recognize_entities(
            user_question
        )


        st.subheader(
            "🔍 Detected Medical Entities"
        )


        found = False


        if entities["Diseases"]:

            found = True

            st.write(
                "🦠 Detected Diseases:"
            )

            for disease in entities["Diseases"]:

                st.write(
                    f"• {disease}"
                )



        if entities["Symptoms"]:

            found = True

            st.write(
                "🤒 Detected Symptoms:"
            )

            for symptom in entities["Symptoms"]:

                st.write(
                    f"• {symptom}"
                )



        if entities["Medicines"]:

            found = True

            st.write(
                "💊 Detected Medicines:"
            )

            for medicine in entities["Medicines"]:

                st.write(
                    f"• {medicine}"
                )



        if entities["Treatments"]:

            found = True

            st.write(
                "🏥 Detected Treatments:"
            )

            for treatment in entities["Treatments"]:

                st.write(
                    f"• {treatment}"
                )



        if not found:

            st.info(
                "No medical entities detected."
            )



        # -----------------------------
        # Medical Answer
        # -----------------------------

        st.subheader(
            "💬 Medical Answer"
        )


        answer = get_answer(
            user_question
        )


        translated_answer = translate_text(
            answer,
            language
        )


        st.write(
            translated_answer
        )



# -----------------------------
# Footer
# -----------------------------

st.markdown("---")


st.caption(
    "Medical Q&A | TF-IDF | Cosine Similarity | "
    "Entity Recognition | Sentiment Analysis | "
    "Research Search | Image Upload | "
    "Multilingual Translation"
)