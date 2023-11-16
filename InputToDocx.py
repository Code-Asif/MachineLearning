from docx import Document

def create_preformatted_document(user_input):
    # Create a new Word document
    doc = Document()

    # Add a heading to the document
    doc.add_heading('Preformatted Document', level=1)

    # Add a placeholder for user input
    doc.add_paragraph(f"User input: {user_input}")

    # Save the document
    doc.save('preformatted_document.docx')

if __name__ == "__main__":
    # Take user input
    user_input = input("Enter text to be inserted into the document: ")

    # Create and save the preformatted document with user input
    create_preformatted_document(user_input)

    print("Document created and saved as 'preformatted_document.docx'")
