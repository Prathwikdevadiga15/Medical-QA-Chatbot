import chromadb

client = chromadb.PersistentClient(
    path="vector_store/chroma_db"
)

collection = client.get_collection(
    name="medical_knowledge"
)

results = collection.get(
    include=["documents", "metadatas"]
)

print("Total documents:", collection.count())

print("\nALL DOCUMENTS:\n")

for i, document in enumerate(results["documents"]):

    print("=" * 60)
    print(f"DOCUMENT {i + 1}")
    print(document)