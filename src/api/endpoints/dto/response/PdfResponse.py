from pydantic import BaseModel

class PDFResponse(BaseModel):
    content: str
