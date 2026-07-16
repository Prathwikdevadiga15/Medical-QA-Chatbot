import os
import xml.etree.ElementTree as ET
import pandas as pd

dataset_path = "dataset/MedQuAD-master"

questions = []
answers = []

for root_folder, dirs, files in os.walk(dataset_path):
    for file in files:
        if file.endswith(".xml"):
            file_path = os.path.join(root_folder, file)

            try:
                tree = ET.parse(file_path)
                root = tree.getroot()

                for qa in root.findall(".//QAPair"):

                    question = qa.find("Question")
                    answer = qa.find("Answer")

                    if question is not None and answer is not None:

                        q = "".join(question.itertext()).strip()
                        a = "".join(answer.itertext()).strip()

                        if q and a:
                            questions.append(q)
                            answers.append(a)

            except Exception as e:
                print("Error:", file, e)

df = pd.DataFrame({
    "Question": questions,
    "Answer": answers
})

os.makedirs("models", exist_ok=True)

df.to_csv("models/medical_qa.csv", index=False)

print("="*50)
print("Dataset processed successfully!")
print("Total Questions:", len(df))
print("="*50)