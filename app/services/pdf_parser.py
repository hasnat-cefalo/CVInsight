import pymupdf4llm


class PDFParser:
    @staticmethod
    def extract_text_from_pdf(file_path: str) -> str:
        with open(file_path, "rb") as file:
            content = pymupdf4llm.to_markdown(file)
            # print(content)
        return content