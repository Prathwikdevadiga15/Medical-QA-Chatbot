import spacy


# Load NLP model
nlp = spacy.load("en_core_web_sm")


# Medical dictionaries

SYMPTOMS = [
    "fever",
    "headache",
    "cough",
    "cold",
    "chest pain",
    "vomiting",
    "fatigue",
    "pain",
    "breathing problem"
]


DISEASES = [
    "diabetes",
    "cancer",
    "covid",
    "asthma",
    "flu",
    "malaria",
    "hypertension"
]


TREATMENTS = [
    "surgery",
    "therapy",
    "exercise",
    "chemotherapy",
    "physiotherapy"
]


MEDICINES = [
    "paracetamol",
    "ibuprofen",
    "aspirin",
    "insulin"
]


def recognize_entities(text):

    text = text.lower()

    detected = {
        "Symptoms": [],
        "Diseases": [],
        "Treatments": [],
        "Medicines": []
    }


    for symptom in SYMPTOMS:
        if symptom in text:
            detected["Symptoms"].append(symptom.title())


    for disease in DISEASES:
        if disease in text:
            detected["Diseases"].append(disease.title())


    for treatment in TREATMENTS:
        if treatment in text:
            detected["Treatments"].append(treatment.title())


    for medicine in MEDICINES:
        if medicine in text:
            detected["Medicines"].append(medicine.title())


    return detected



# Testing

if __name__ == "__main__":

    query = input("Enter medical question: ")

    result = recognize_entities(query)

    print("\nDetected Entities")

    for key,value in result.items():
        print(key,":",value)