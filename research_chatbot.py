from summarizer import summarize_abstract
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load research papers
data = pd.read_csv("./research_data/research_papers.csv")

papers = data["Abstract"].astype(str).tolist()

# Create TF-IDF model
vectorizer = TfidfVectorizer(stop_words="english")
paper_vectors = vectorizer.fit_transform(papers)


def search_paper(question):

    question_vector = vectorizer.transform([question])

    similarity = cosine_similarity(
        question_vector,
        paper_vectors
    )

    best_index = similarity.argmax()
    score = similarity[0][best_index]

    if score < 0.1:
        return "No relevant research paper found."

    result = data.iloc[best_index]

    summary = summarize_abstract(result["Abstract"])

    answer = f"""
📚 Research Paper

Title:
{result['Title']}

Category:
{result['Category']}

Summary:
{summary}
"""

    return answer