import fitz  # PyMuPDF

def pdf_to_text(pdf_path, output_text_file):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    text_content = ""

    # Iterate through the pages
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text()
        text_content += text + "\n"

    # Save the extracted text to a file
    with open(output_text_file, 'w', encoding='utf-8') as file:
        file.write(text_content)

    print(f"Text extracted and saved to {output_text_file}")

# Example usage:
pdf_path = 'DBMS INTERVIEW QUESTIONS .pdf'
output_text_file = 'output_text.txt'
pdf_to_text(pdf_path, output_text_file)
