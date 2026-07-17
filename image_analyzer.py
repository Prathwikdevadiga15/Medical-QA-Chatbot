def analyze_image(uploaded_file, question):

    if uploaded_file is None:
        return "Please upload an image."

    if question.strip() == "":
        return "Please enter a question about the image."

    return (
        "Image uploaded successfully.\n\n"
        f"Question: {question}\n\n"
        "This project currently demonstrates the image upload workflow. "
        "Actual AI image analysis can be added later using a vision model."
    )