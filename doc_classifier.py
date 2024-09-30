import pytesseract
from PIL import Image

# Define unique keywords for classification
transaction_keywords = [
    "Invoice", "Amount Due", "Subtotal", "Discount", 
    "Consulting", "Services", "Materials", "Due Date", 
    "Rate", "Quantity", "Total:", "Deposit Due", "Ticket Completed"
]

insurance_keywords = [
    "Policy Holder", "Insurance Company", "Policy Number", 
    "Coverage", "Limits of Coverage", "Liability", 
    "Deductible", "Policy Premium", "Inception Date", 
    "Expiration Date", "Home Owners Policy", 
    "Insuring Agreement", "Reporting a Claim"
]

def classify_document(img):
    """
    Classifies a document as either 'Transaction' or 'Insurance' based on its text content.

    Parameters:
        img (PIL.Image): The image to classify.

    Returns:
        str: The classification result ('Transaction', 'Insurance', or 'Unclassified').
    """
    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(img)

    # Initialize counters for keyword matches
    transaction_count = sum(1 for keyword in transaction_keywords if keyword in text)
    insurance_count = sum(1 for keyword in insurance_keywords if keyword in text)

    # Classify based on the presence of keywords
    if transaction_count > insurance_count:
        return "Transaction"
    elif insurance_count > transaction_count:
        return "Insurance"
    else:
        return "Unclassified"



if __name__=="__main__":
    img = Image.open("/mnt/d/exam/Document/Transaction/100.png")
    print(classify_document(img))