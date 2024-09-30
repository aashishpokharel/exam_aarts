import streamlit as st
from transformers import pipeline
from doc_classifier import classify_document
from PIL import Image
import pandas as pd  # Import pandas for table display
from pdf2image import convert_from_path  # Import pdf2image for PDF to image conversion
import tempfile  # Import tempfile for temporary file handling

# Initialize the NLP pipeline
nlp = pipeline("document-question-answering", model="impira/layoutlm-document-qa")

# Define questions based on document types
questions_dict = {
    "Transaction": ["Transaction Date", "Transaction Description", "Total amount", "Address"], 
    "Insurance": ["Start Date", "End Date", "Policy Number", "Provider Name", "Term", "Premium", "Address of Policy"]
}

def main():
    st.title("Document Question Answering App")

    # Upload file (image or PDF)
    uploaded_file = st.file_uploader("Choose an image or PDF...", type=["jpg", "jpeg", "png", "pdf"])
    
    if uploaded_file:
        # Initialize the image variable
        image = None

        if uploaded_file.type == "application/pdf":
            # Process PDF using pdf2image
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(uploaded_file.read())  # Write the uploaded PDF to a temporary file
                tmp_file_path = tmp_file.name
            
            # Convert PDF to images
            try:
                images = convert_from_path(tmp_file_path)  # Convert PDF to images
                image = images[0]  # Use the first page as an image
            except Exception as e:
                st.error(f"Error converting PDF to image: {e}")
                return
        else:
            # Process image file
            try:
                image = Image.open(uploaded_file).convert("RGB")  # Ensure the image is in RGB format
            except Exception as e:
                st.error(f"Error opening image file: {e}")
                return
        
        st.image(image, caption="Uploaded Document.", use_column_width=True)
        st.write("")
        st.write("Classifying document...")

        # Classify document
        doctype = classify_document(image)
        st.write(f"Document Type: {doctype}")
        
        if doctype in questions_dict:
            questions = questions_dict[doctype]

            # Prepare answers
            answers = []
            for question in questions:
                # Get answer from NLP model
                result = nlp(image, f"what is {question}?")[0]  # Get the first result
                score = result['score'] if 'score' in result else None
                answer = result['answer'] if 'answer' in result else "No answer found"
                
                answers.append({"Question": question, "Answer": answer, "Confidence Score": score})

            # Create a DataFrame and display it as a table
            answers_df = pd.DataFrame(answers)
            st.table(answers_df)  # Display answers in table form

        else:
            st.write("Document type not recognized.")

if __name__ == "__main__":
    main()
