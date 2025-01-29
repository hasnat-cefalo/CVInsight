import os
import logging
from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.pdf_parser import PDFParser
from app.services.cv_processor import CVProcessor
from app.models.cv_model import CVModel

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/parse-cv/", response_model=CVModel)
async def parse_cv(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF")

    file_path = f"/tmp/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    try:
        text = PDFParser.extract_text_from_pdf(file_path)
        cv_data = CVProcessor.parse_cv(text)
        logger.info("successfully parsed CV")
    finally:
        os.remove(file_path)
        logger.info("Successfully removed CV")

    return cv_data
