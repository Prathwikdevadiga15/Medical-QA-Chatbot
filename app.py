import streamlit as st

from dynamic_chatbot import get_dynamic_answer
from entity_recognition import recognize_entities
from sentiment import analyze_sentiment
from research_chatbot import search_paper
from image_analyzer import analyze_image


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Medical AI Assistant",
    page_icon="🩺",
    layout="wide"
)


# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🤖 AI Assistants")

assistant_mode = st.sidebar.selectbox(
    "Choose an assistant:",
    [
        "🩺 Medical Assistant",
        "📚 Research Assistant",
        "🖼️ Multimodal Assistant"
    ]
)


# =====================================================
# MAIN TITLE
# =====================================================

st.title("🩺 Medical AI Assistant")

st.write(
    "An AI-powered assistant with a dynamically expanding "
    "knowledge base."
)


# =====================================================
# 1. MEDICAL ASSISTANT
# =====================================================

if assistant_mode == "🩺 Medical Assistant":

    st.header("🩺 Dynamic Medical Q&A Chatbot")

    st.write(
        "Ask a medical question. The chatbot searches the "
        "dynamically updated vector database."
    )

    user_question = st.text_input(
        "Enter your medical question:"
    )

    if st.button("🔍 Get Medical Answer"):

        if user_question.strip():

            # Search the dynamic vector database
            answer = get_dynamic_answer(
                user_question
            )

            st.subheader("💡 Answer")

            st.write(answer)

            # -----------------------------
            # Medical Entity Recognition
            # -----------------------------

            try:

                entities = recognize_entities(
                    user_question
                )

                if entities:

                    st.subheader(
                        "🔎 Detected Medical Entities"
                    )

                    st.write(entities)

            except Exception as error:

                st.warning(
                    f"Entity recognition unavailable: {error}"
                )

            # -----------------------------
            # Sentiment Analysis
            # -----------------------------

            try:

                sentiment_result = analyze_sentiment(
                    user_question
                )

                st.subheader(
                    "😊 Question Sentiment"
                )

                st.write(sentiment_result)

            except Exception as error:

                st.warning(
                    f"Sentiment analysis unavailable: {error}"
                )

        else:

            st.warning(
                "Please enter a medical question."
            )


# =====================================================
# 2. RESEARCH ASSISTANT
# =====================================================

elif assistant_mode == "📚 Research Assistant":

    st.header("📚 Scientific Research Assistant")

    st.write(
        "Search for scientific research information."
    )

    research_question = st.text_input(
        "Enter your research topic:"
    )

    if st.button("🔍 Search Research Papers"):

        if research_question.strip():

            try:

                result = search_paper(
                    research_question
                )

                st.subheader(
                    "📄 Research Results"
                )

                st.write(result)

            except Exception as error:

                st.error(
                    f"Research search failed: {error}"
                )

        else:

            st.warning(
                "Please enter a research topic."
            )


# =====================================================
# 3. MULTIMODAL ASSISTANT
# =====================================================

elif assistant_mode == "🖼️ Multimodal Assistant":

    st.header("🖼️ Multimodal Medical Assistant")

    st.write(
        "Upload an image for analysis."
    )

    uploaded_image = st.file_uploader(
        "Upload a medical image:",
        type=[
            "jpg",
            "jpeg",
            "png"
        ]
    )

    if uploaded_image is not None:

        st.image(
            uploaded_image,
            caption="Uploaded Medical Image",
            use_container_width=True
        )

        if st.button("🔍 Analyze Image"):

            try:

                result = analyze_image(
                    uploaded_image
                )

                st.subheader(
                    "🧠 Image Analysis"
                )

                st.write(result)

            except Exception as error:

                st.error(
                    f"Image analysis failed: {error}"
                )


# =====================================================
# DISCLAIMER
# =====================================================

st.sidebar.markdown("---")

st.sidebar.warning(
    "⚠️ This chatbot is for educational and informational "
    "purposes only. It is not a substitute for professional "
    "medical advice."
)