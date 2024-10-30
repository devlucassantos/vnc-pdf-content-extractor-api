from pydantic import BaseModel

class PDFUrlRequest(BaseModel):
    pdf_url: str
