# 🏥 Medical Q&A Chatbot

## 📌 Overview

The **Medical Q&A Chatbot** is a specialized healthcare assistant built using **Python, Streamlit, and the MedQuAD dataset**. It helps users find answers to medical questions by retrieving the most relevant information from a structured medical knowledge base.

The chatbot uses **TF-IDF retrieval** to identify the most relevant medical question-answer pairs and **Medical Entity Recognition (NER)** to extract important medical terms such as symptoms, diseases, treatments, and medicines from user queries.

---

## 🚀 Features

- 🏥 Medical Question Answering
- 📚 MedQuAD Dataset Integration
- 🔍 TF-IDF Based Information Retrieval
- 🧬 Medical Entity Recognition (NER)
- 💊 Identification of Symptoms, Diseases, Treatments, and Medicines
- 🎨 Interactive Streamlit Web Interface
- ⚡ Fast and Accurate Medical Answer Retrieval

---

## 🛠 Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- spaCy
- TF-IDF Vectorizer
- NumPy

---

## 📂 Project Structure

```
Medical-QA-Chatbot/
│
├── app.py
├── chatbot.py
├── entity_recognition.py
├── summarizer.py
├── requirements.txt
├── README.md
├── models/
│   ├── medical_model.pkl
│   └── tfidf_vectorizer.pkl
├── data/
│   └── MedQuAD.csv
└── report/
    └── Medical_QA_Report.pdf
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Prathwikdevadiga15/Medical-QA-Chatbot.git
```

### Move into the project directory

```bash
cd Medical-QA-Chatbot
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. The user enters a medical question.
2. The chatbot preprocesses the input.
3. TF-IDF converts the question into numerical features.
4. Cosine similarity retrieves the most relevant question from the MedQuAD dataset.
5. Medical Entity Recognition identifies symptoms, diseases, treatments, and medicines.
6. The chatbot displays the most relevant medical answer through the Streamlit interface.

---

## 📚 Dataset

This project uses the **MedQuAD (Medical Question Answer Answering Dataset)**, which contains thousands of medically reviewed question-answer pairs collected from trusted healthcare organizations, including:

- ADAM
- Cancer.gov
- NIDDK
- Drugs
- NHLBI
- MedlinePlus

The dataset enables the chatbot to retrieve reliable answers for a wide range of medical queries.

---

## 🧪 Example

### User Question

**What are the symptoms of diabetes?**

### Medical Entities Detected

- Disease: Diabetes
- Symptoms

### Chatbot Response

Common symptoms of diabetes include increased thirst, frequent urination, fatigue, blurred vision, unexplained weight loss, and slow wound healing.

---

## 🎯 Assignment Objectives Achieved

### Task 2 – Medical Q&A Chatbot

- ✅ MedQuAD Dataset Integration
- ✅ TF-IDF Retrieval Mechanism
- ✅ Medical Entity Recognition
- ✅ Medical Question Answering
- ✅ Streamlit Web Interface

---

## 🔮 Future Improvements

- Voice-based medical assistant
- Multilingual support
- Retrieval-Augmented Generation (RAG)
- Integration with latest medical databases
- Medical document question answering

---

## 👨‍💻 Author

**Prathwik H Devadiga**

GitHub: https://github.com/Prathwikdevadiga15

---

⭐ If you found this project useful, consider giving it a star.
