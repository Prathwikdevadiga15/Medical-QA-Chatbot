import chromadb
from sentence_transformers import SentenceTransformer


# Load the embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# Create a persistent ChromaDB client
client = chromadb.PersistentClient(
    path="vector_store/chroma_db"
)


# Create or access the medical knowledge collection
collection = client.get_or_create_collection(
    name="medical_knowledge"
)


def add_document(document_id, text, metadata):
    """
    Add one document to the vector database.
    """

    embedding = embedding_model.encode(
        text
    ).tolist()

    collection.add(
        ids=[document_id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[metadata]
    )


def search_documents(query, number_of_results=3):

    query_embedding = embedding_model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=number_of_results
    )

    return results
    """
    Search the vector database for relevant information.
    """

    query_embedding = embedding_model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=number_of_results
    )

    return results


def get_document_count():
    """
    Return the number of stored documents.
    """

    return collection.count()