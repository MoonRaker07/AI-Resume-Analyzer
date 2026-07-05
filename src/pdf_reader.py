import pdfplumber


def extract_text_from_pdf(pdf_file):
    """
    Extracts text from every page of a PDF file.

    Parameters:
        pdf_file: Uploaded PDF file from Streamlit

    Returns:
        Extracted text as a string
    """

    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text