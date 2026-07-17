import pandas as pd

# Read existing dataset
old_data = pd.read_csv("models/medical_qa.csv")

# Read new questions
new_data = pd.read_csv("datasets/new_questions.csv")

# Merge datasets
updated_data = pd.concat([old_data, new_data], ignore_index=True)

# Remove duplicate questions
updated_data = updated_data.drop_duplicates(subset=["Question"])

# Save updated dataset
updated_data.to_csv("models/medical_qa.csv", index=False)

print("✅ Dataset updated successfully!")
print("Total Questions:", len(updated_data))