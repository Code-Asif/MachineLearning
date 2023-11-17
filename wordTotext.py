# pip install python-docx
# pip install PyPDF2

import docx2txt
import PyPDF2

def extract_text_from_docx(docx_file):
    text = docx2txt.process(docx_file)
    return text

def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.numPages
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

if __name__ == "__main__":
    # Replace these file paths with the path to your own documents
    docx_file_path = "rentalAgreement.docx"
    # pdf_file_path = "path/to/your/document.pdf"

    # Extract text from the Word document
    docx_text = extract_text_from_docx(docx_file_path)

    # Extract text from the PDF document
    # pdf_text = extract_text_from_pdf(pdf_file_path)

    # Print or use the extracted text as needed
    print("Text from Word document:")
    print(docx_text)

    # print("\nText from PDF document:")
    # print(pdf_text)

    # # You can store the text in variables if needed
    # combined_text = docx_text + "\n" + pdf_text
    # print("\nCombined text:")
    # print(combined_text)
