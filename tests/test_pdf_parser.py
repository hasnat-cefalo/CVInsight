import unittest
from app.services.pdf_parser import PDFParser

class TestPDFParser(unittest.TestCase):
    def test_extract_text_from_pdf(self):
        text = PDFParser.extract_text_from_pdf("path/to/test.pdf")
        self.assertIsInstance(text, list)
        self.assertTrue(len(text) > 0)

if __name__ == "__main__":
    unittest.main()
