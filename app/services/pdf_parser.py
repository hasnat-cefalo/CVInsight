import fitz

def extract_with_pymupdf(pdf_path):
    doc = fitz.open(pdf_path)
    extracted_data = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text_blocks = page.get_text("blocks")  # Extract text blocks with coordinates
        links = page.get_links()  # Extract links

        for block in text_blocks:
            x0, y0, x1, y1, text, block_no, block_type = block
            if text.strip():  # Ignore empty blocks
                # Find links that are within or near this text block
                associated_links = []
                for link in links:
                    link_rect = fitz.Rect(link["from"])
                    # Check if the link is near or within the text block
                    if link_rect.intersects(fitz.Rect(x0, y0, x1, y1)):
                        associated_links.append(link["uri"])

                # Store the text and its associated links (without the word "Text")
                extracted_data.append({
                    "content": text.strip(),  # Renamed "text" to "content"
                    "links": associated_links
                })

    return extracted_data

class PDFParser:

    @staticmethod
    def extract_text_from_pdf(file_path: str) -> str:
        pymupdf_data = extract_with_pymupdf(file_path)
        all_text=""
        for item in pymupdf_data:
            all_text += f"{item['content']}\n"
            if item["links"]:
                all_text += f"Links: {', '.join(item['links'])}\n"
            all_text += "\n"
        return all_text
