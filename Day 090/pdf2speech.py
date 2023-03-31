import PyPDF2
import pyttsx3

# Open the PDF file in read-binary mode
pdf_file = open('example.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF file
num_pages = len(pdf_reader.pages)

# Initialize the text variable
text = ""

# Loop through all the pages and extract the text
for page in range(num_pages):
    page_obj = pdf_reader.pages[0]
    text += page_obj.extract_text()

# Close the PDF file
pdf_file.close()

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Convert the text to speech
engine.say(text)
engine.runAndWait()
