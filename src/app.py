import logging
import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from src.api.handlers.PdfContentExtractionHandler import pdfContentExtractionRouter

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv(os.path.join(os.path.dirname(__file__), 'api/config', '.env'))

app = FastAPI(
    title="VNC PDF Content Extractor API",
    description="API responsible for extracting text from a PDF file provided via a URL.",
    version="v1",
    contact={
        "name": "Você na Câmara",
        "email": "email.vocenacamara@gmail.com",
    },
    docs_url="/api/documentation"
)

app.include_router(pdfContentExtractionRouter)

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host=host, port=port)
