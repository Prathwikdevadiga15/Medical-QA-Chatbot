from vector_database import (
    add_document,
    search_documents,
    get_document_count
)

add_document(
    document_id="test_001",
    text="Diabetes is a chronic disease that affects blood sugar levels.",
    metadata={
        "source": "Test Data"
    }
)

print("Total documents:", get_document_count())

results = search_documents("What is asthma?")

print("\nSearch Results:")
print(results)