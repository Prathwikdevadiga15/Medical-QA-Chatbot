## 🔄 Dynamic Knowledge Base

The Medical AI Assistant uses a dynamic knowledge-base system that allows new medical information to be incorporated into the chatbot over time without retraining the complete machine-learning model.

### Workflow

New Medical Information
        ↓
new_questions.csv
        ↓
scheduler.py
        ↓
knowledge_updater.py
        ↓
Duplicate Detection
        ↓
Sentence Embeddings
        ↓
ChromaDB Vector Database
        ↓
Semantic Search
        ↓
Dynamic Medical Chatbot
        ↓
Updated Medical Response

### Components

- `new_questions.csv` — Stores newly added medical question-answer pairs.
- `knowledge_updater.py` — Reads new information and adds it to the vector database.
- `scheduler.py` — Periodically checks for new medical information.
- ChromaDB — Stores medical knowledge as vector embeddings.
- `dynamic_chatbot.py` — Performs semantic search and retrieves relevant answers.
- `app.py` — Provides the Streamlit user interface.

### Duplicate Prevention

The system checks whether a question already exists in the vector database. Existing questions are skipped, preventing duplicate knowledge from being added.

### Testing Result

A new question was added:

**Question:** What is migraine?

The system successfully:

1. Detected the new question.
2. Added it to the vector database.
3. Increased the total document count.
4. Retrieved the information through the chatbot.
5. Returned the correct answer to the user.

### Example Result

**User Question:**

What is migraine?

**Chatbot Answer:**

Migraine is a neurological condition that can cause severe headache and other symptoms.

### Outcome

The dynamic knowledge-base system successfully enables the chatbot to incorporate new medical information over time without requiring complete model retraining.