import PyPDF2


def extract_pdf_text(pdf_path):

    try:
        with open(pdf_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)

            full_text = ""

            for page in pdf_reader.pages:
                page_text = page.extract_text()

                if page_text:
                    full_text += page_text + "\n"

            return full_text

    except Exception as e:
        raise Exception(f"PDF Extraction Error: {str(e)}")