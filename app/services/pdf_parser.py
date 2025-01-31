import PyPDF2


class PDFParser:
    @staticmethod
    def extract_text_from_pdf(file_path: str) -> str:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            content = ""

            for page in reader.pages:
                # Extract visible text
                text = page.extract_text()
                if text:
                    content += "\n".join(line.rstrip() for line in text.split("\n") if line)
                    content += "\n"

                # Extract hyperlinks (annotations)
                if "/Annots" in page:
                    for annot in page["/Annots"]:
                        annot_obj = annot.get_object()
                        if "/A" in annot_obj and "/URI" in annot_obj["/A"]:
                            content += f"LINK: {annot_obj['/A']['/URI']}\n"

        return content