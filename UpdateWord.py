from docx import Document

def fill_rental_agreement_template(name, date, address, agreement_type):
    # Load the rental agreement template
    doc = Document('rental_agreement_template.docx')

    # Define placeholders in the template
    placeholders = {
        'NamePlaceholder': name,
        'DatePlaceholder': date,
        'AddressPlaceholder': address,
        'AgreementTypePlaceholder': agreement_type,
        # Add more placeholders as needed
    }

    # Iterate through paragraphs in the document
    for paragraph in doc.paragraphs:
        for placeholder, value in placeholders.items():
            if placeholder in paragraph.text:
                # Replace the placeholder with user input
                paragraph.text = paragraph.text.replace(placeholder, str(value))

    # Save the filled document
    doc.save('filled_rental_agreement.docx')

if __name__ == "__main__":
    # Take user input
    name = input("Enter your name: ")
    date = input("Enter the date: ")
    address = input("Enter your address: ")
    agreement_type = input("Enter the type of agreement: ")

    # Fill the rental agreement template with user input
    fill_rental_agreement_template(name, date, address, agreement_type)

    print("Filled rental agreement document saved as 'filled_rental_agreement.docx'")
