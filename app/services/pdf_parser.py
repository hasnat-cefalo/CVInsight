import PyPDF2

class PDFParser:
    @staticmethod
    def extract_text_from_pdf(file_path: str) -> str:
        # Use PdfReader instead of PdfFileReader
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text