import chromadb
from sentence_transformers import SentenceTransformer


# =====================================================
# CONFIGURATION
# =====================================================

DATABASE_PATH = "vector_store/chroma_db"

COLLECTION_NAME = "medical_knowledge"

# Smaller ChromaDB distance = better match
MAX_DISTANCE = 1.2


# =====================================================
# LOAD EMBEDDING MODEL
# =====================================================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# =====================================================
# CONNECT TO VECTOR DATABASE
# =====================================================

client = chromadb.PersistentClient(
    path=DATABASE_PATH
)

collection = client.get_collection(
    name=COLLECTION_NAME
)


# =====================================================
# GET ANSWER FROM DYNAMIC KNOWLEDGE BASE
# =====================================================

def get_dynamic_answer(user_question):

    # Search the vector database
    results = collection.query(
        query_texts=[
            user_question
        ],
        n_results=5
    )


    # Check if documents were found
    if not results.get("documents"):

        return (
            "Sorry, I could not find reliable information "
            "about this question in my current knowledge base."
        )


    documents = results["documents"][0]

    distances = results["distances"][0]


    # No documents found
    if not documents:

        return (
            "Sorry, I could not find reliable information "
            "about this question in my current knowledge base."
        )


    # Get the best matching document
    best_document = documents[0]

    best_distance = distances[0]


    # Print for debugging
    print(
        "\nSearch distance:",
        best_distance
    )

    print(
        "\nBest matching document:"
    )

    print(
        best_document
    )


    # Check relevance
    if best_distance > MAX_DISTANCE:

        return (
            "Sorry, I could not find reliable information "
            "about this question in my current knowledge base."
        )


    # =================================================
    # RETURN ONLY THE ANSWER
    # =================================================

    if "Answer:" in best_document:

        answer = best_document.split(
            "Answer:",
            1
        )[1].strip()

        return answer


    # If document has no Answer: label
    return best_document


# =====================================================
# DIRECT TERMINAL TEST
# =====================================================

if __name__ == "__main__":

    print("=" * 60)

    print(
        "🩺 Dynamic Medical Knowledge Chatbot"
    )

    print("=" * 60)


    while True:

        question = input(
            "\nAsk a medical question "
            "(type 'exit' to quit): "
        )


        # Exit chatbot
        if question.lower().strip() == "exit":

            print(
                "\nChatbot stopped."
            )

            break


        # Empty question check
        if not question.strip():

            print(
                "\nPlease enter a question."
            )

            continue


        # Get dynamic answer
        answer = get_dynamic_answer(
            question
        )


        print(
            "\n💡 Answer:"
        )

        print(
            answer
        )