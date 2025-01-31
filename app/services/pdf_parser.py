import PyPDF2


class PDFParser:
    @staticmethod
    def extract_text_from_pdf(file_path: str) -> str:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            content = ""
            for page in reader.pages:
                text = page.extract_text()
                for line in text.split('\n'):
                    line = line.rstrip()
                    if line:
                        content += line
                        content += '\n'
        return content
