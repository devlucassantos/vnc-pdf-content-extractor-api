import asyncio
import logging

import validators
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
        408: {
            "description": "The timeout for extracting the PDF content has been exceeded",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Request timeout: Extracting PDF content exceeded processing timeout"
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
                                "type": "invalid_url",
                                "loc": ["body", "pdf_url"],
                                "msg": "Input should be a valid URL",
                                "input": "test.com"
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
                        "detail": "Error downloading the PDF: No /Root object! - Is this really a PDF?"
                    }
                }
            }
        },
    }
)
async def extract_content(pdf_url_request: PDFUrlRequest):
    pdf_url = pdf_url_request.pdf_url

    logging.info(f"Attempting to download PDF from <{pdf_url}>")

    if not validators.url(pdf_url):
        logging.error(f"Error downloading the PDF from <{pdf_url}>: PDF URL is invalid")
        raise HTTPException(status_code=422, detail=[{
                "type": "invalid_url",
                "loc": ["body", "pdf_url"],
                "msg": "Input should be a valid URL",
                "input": pdf_url
            }])

    cancel_event = asyncio.Event()

    try:
        pdf_content = await asyncio.wait_for(asyncio.to_thread(extract_content_from_pdf_url, pdf_url,
            cancel_event), timeout=45)
    except asyncio.TimeoutError:
        cancel_event.set()
        logging.error(f"Error downloading the PDF from <{pdf_url}>: Extracting PDF content exceeded processing timeout")
        raise HTTPException(status_code=408, detail="Request timeout: Extracting PDF content exceeded processing timeout")
    except Exception as e:
        logging.error(f"Error downloading the PDF from <{pdf_url}>: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error downloading the PDF: {str(e)}")

    logging.info(f"Content extraction from PDF <{pdf_url}> successful. Returning extracted text.")
    return JSONResponse(content={"content": pdf_content})
