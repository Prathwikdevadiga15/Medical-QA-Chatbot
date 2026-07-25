import pandas as pd
import hashlib

from vector_database import add_document
import chromadb


# ==========================================
# FILE PATH
# ==========================================

CSV_FILE = "datasets/new_questions.csv"


# ==========================================
# CONNECT TO VECTOR DATABASE
# ==========================================

client = chromadb.PersistentClient(
    path="vector_store/chroma_db"
)

collection = client.get_collection(
    name="medical_knowledge"
)


# ==========================================
# CREATE UNIQUE DOCUMENT ID
# ==========================================

def create_document_id(question):

    return hashlib.md5(
        question.strip().lower().encode()
    ).hexdigest()


# ==========================================
# UPDATE KNOWLEDGE BASE
# ==========================================

def update_knowledge_base():

    print("\nStarting knowledge base update...")

    # Read CSV file
    data = pd.read_csv(
        CSV_FILE,
        header=None,
        names=["question", "answer"]
    )

    added_count = 0
    skipped_count = 0

    # Process every row
    for index, row in data.iterrows():

        question = str(
            row["question"]
        ).strip()

        answer = str(
            row["answer"]
        ).strip()

        # Skip empty rows
        if not question or not answer:

            continue

        # Create unique ID
        document_id = create_document_id(
            question
        )

        # Check whether ID already exists
        existing = collection.get(
            ids=[document_id]
        )

        if existing["ids"]:

            print(
                f"Skipped existing question: {question}"
            )

            skipped_count += 1

            continue

        # Create document
        document_text = (
            f"Question: {question}\n"
            f"Answer: {answer}"
        )

        # Add new document
        add_document(
            document_id=document_id,
            text=document_text,
            metadata={
                "source": "new_questions.csv",
                "type": "dynamic_update"
            }
        )

        print(
            f"Added new question: {question}"
        )

        added_count += 1

    print("\nKnowledge base update completed.")

    print(
        f"New documents added: {added_count}"
    )

    print(
        f"Existing documents skipped: {skipped_count}"
    )

    print(
        f"Total documents in database: "
        f"{collection.count()}"
    )


# ==========================================
# RUN UPDATE
# ==========================================

if __name__ == "__main__":

    update_knowledge_base()