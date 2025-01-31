import logging
import os
import traceback

from fastapi import APIRouter, File, UploadFile, HTTPException, Query

from app.models.cv_model import CVModel
from app.services.cv_processor import CVProcessor
from app.services.pdf_parser import PDFParser
from app.utils.models import ModelType

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/parse-cv/", response_model=CVModel)
async def parse_cv(file: UploadFile = File(...),
                   model_type: ModelType = Query(..., description="Parsing model to use")):
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
        cv_data = CVProcessor.parse_cv(text=text, model_type=model_type)
        logger.info("successfully parsed CV")
        return cv_data
    except Exception as e:
        logger.error(f"Error processing CV: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        # Ensure the temporary file is deleted
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                logger.info(f"Temporary file {file_path} removed successfully")
        except Exception as e:
            logger.error(f"Failed to remove temporary file: {e}")
