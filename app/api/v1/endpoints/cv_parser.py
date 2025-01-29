import logging
import os
from enum import Enum

from fastapi import APIRouter, File, UploadFile, HTTPException, Query

from app.models.cv_model import CVModel
from app.services.cv_processor import CVProcessor
from app.services.pdf_parser import PDFParser

logger = logging.getLogger(__name__)
router = APIRouter()


class ServiceType(str, Enum):
    NLP = "nlp"
    CHATGPT = "chatgpt"
    DEEPSEEK = "deepseek"


@router.post("/parse-cv/", response_model=CVModel)
async def parse_cv(file: UploadFile = File(...),
                   service_type: ServiceType = Query(..., description="Parsing method to use")):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF")

    file_path = f"/tmp/{file.filename}"
    try:
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())
        logger.info(f"File saved temporarily at {file_path}")
    except Exception as e:
        logger.error(f"Failed to save file: {e}")
        raise HTTPException(status_code=500, detail="Failed to read or save uploaded file")

    try:
        text = PDFParser.extract_text_from_pdf(file_path)
        cv_data = CVProcessor.parse_cv(text=text, service_type=service_type)
        logger.info("successfully parsed CV")
        return cv_data
    except Exception as e:
        logger.error(f"Error processing CV: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        # Ensure the temporary file is deleted
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                logger.info(f"Temporary file {file_path} removed successfully")
        except Exception as e:
            logger.error(f"Failed to remove temporary file: {e}")


