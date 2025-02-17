import logging
import os
import shutil
import traceback
from pathlib import Path

from app.services.cv_processor import CVProcessor
from app.services.pdf_parser import PDFParser
from app.utils.models import ModelType

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define paths
INPUT_FOLDER = "./cv_uploads"  # Folder containing PDFs
OUTPUT_FOLDER = "./cv_processed_new"  # Folder to store text and JSON
PROCESSED_FOLDER = "./cv_processed_pdfs_new"  # Folder to store processed PDFs

# Ensure output and processed directories exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

models = [ ModelType.MISTRAL, ModelType.QWEN_1_8B,
          ModelType.QWEN_14B]


def process_cv_files():
    pdf_files = list(Path(INPUT_FOLDER).glob("*.pdf"))

    if not pdf_files:
        logger.info("No PDF files found in input folder.")
        return

    for pdf_file in pdf_files:
        try:
            logger.info(f"Processing {pdf_file.name}")

            # Extract text from PDF
            text = PDFParser.extract_text_from_pdf(str(pdf_file))
            text_filename = pdf_file.stem + ".txt"
            text_path = Path(OUTPUT_FOLDER) / text_filename

            with open(text_path, "w", encoding="utf-8") as text_file:
                text_file.write(text)
            logger.info(f"Extracted text saved: {text_path}")

            for model in models:
                try:
                    # Parse CV to structured JSON
                    cv_data = CVProcessor.parse_cv(text=text, model_type=model)
                    json_filename = pdf_file.stem + f"{model}.json"
                    json_path = Path(OUTPUT_FOLDER) / json_filename

                    with open(json_path, "w", encoding="utf-8") as json_file:
                        json_file.write(cv_data.model_dump_json(indent=4))
                    logger.info(f"Parsed JSON saved: {json_path}")
                except Exception as e:
                    print(e)
                    continue

            # Move the processed PDF to the processed folder
            processed_pdf_path = Path(PROCESSED_FOLDER) / pdf_file.name
            shutil.move(str(pdf_file), str(processed_pdf_path))
            logger.info(f"Moved processed PDF to: {processed_pdf_path}")

        except Exception as e:
            logger.error(f"Error processing {pdf_file.name}: {e}")
            logger.error(traceback.format_exc())


if __name__ == "__main__":
    process_cv_files()
