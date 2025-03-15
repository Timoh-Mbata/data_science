import pytesseract
from PIL import Image
import streamlit as st

# Set the path to your Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Title of the web app
st.title("OCR Text Extraction from Image")

# Instructions for users
st.write("Upload an image file to extract text using Tesseract OCR.")

# Upload image
uploaded_image = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

# If an image is uploaded
if uploaded_image is not None:
    # Open the image using PIL
    image = Image.open(uploaded_image)
    
    # Display the image
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # OCR: Extract text from the image
    text = pytesseract.image_to_string(image)
    
    # Display the extracted text
    st.subheader("Extracted Text:")
    st.write(text)

