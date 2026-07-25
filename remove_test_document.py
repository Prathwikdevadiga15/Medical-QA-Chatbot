import chromadb

client = chromadb.PersistentClient(
    path="vector_store/chroma_db"
)

collection = client.get_collection(
    name="medical_knowledge"
)

collection.delete(
    ids=["test_001"]
)

print("Test document removed.")
print("Total documents:", collection.count())