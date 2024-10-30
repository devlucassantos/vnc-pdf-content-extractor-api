import logging

import requests
from fastapi import HTTPException, APIRouter
from fastapi.responses import JSONResponse

from src.api.endpoints.dto.request.PdfUrlRequest import PDFUrlRequest
from src.api.endpoints.dto.response.PdfResponse import PDFResponse
from src.service.PdfContentExtractionService import extract_content_from_pdf_url

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

pdfContentExtractionRouter = APIRouter(prefix="/api/v1")

@pdfContentExtractionRouter.post(
    path="/extract-content",
    tags=["PDF Content Extraction"],
    response_model=PDFResponse,
    summary="Extract content from a PDF by providing its URL",
    description="This endpoint allows users to submit a URL pointing to a PDF file. The API downloads the PDF, extracts the text from all pages, and returns the extracted text.",
    responses={
        200: {
            "description": "Successful request",
            "content": {
                "application/json": {
                    "example": {
                        "content": "Extracted text from the PDF..."
                    }
                }
            }
        },
        400: {
            "description": "Badly formatted request",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Failed to download PDF"
                    }
                }
            }
        },
        422: {
            "description": "Some of the data provided is invalid",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "type": "string_type",
                                "loc": [
                                    "body",
                                    "pdf_url"
                                ],
                                "msg": "Input should be a valid string",
                                "input": 1
                            }
                        ]
                    }
                }
            }
        },
        500: {
            "description": "An unexpected error occurred while processing the request",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "No /Root object! - Is this really a PDF?"
                    }
                }
            }
        },
    }
)
def extract_content(pdf_url_request: PDFUrlRequest):
    pdf_url = pdf_url_request.pdf_url

    try:
        logging.info(f"Attempting to download PDF from <{pdf_url}>")

        pdf_content = extract_content_from_pdf_url(pdf_url)

        logging.info(f"Content extraction from PDF <{pdf_url}> successful. Returning extracted text.")
        return JSONResponse(content={"content": pdf_content})

    except ValueError as e:
        logging.error(f"Error downloading PDF: The provided pdf_url <{pdf_url}> could not be executed successfully")
        raise HTTPException(status_code=400, detail="Failed to download PDF")

    except requests.exceptions.RequestException as e:
        logging.error(f"Error downloading PDF: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error downloading PDF: {str(e)}")

    except Exception as e:
        logging.error(f"Internal server error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
