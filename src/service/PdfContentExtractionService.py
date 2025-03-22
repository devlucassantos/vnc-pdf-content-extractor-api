import logging
import os
import tempfile

import pdfplumber
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_content_from_pdf_url(pdf_url, cancel_event) -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url=pdf_url, headers=headers, stream=True)
    if response.status_code != 200:
        error_message = f"Failed to download PDF from <{pdf_url}>: [Status code: {response.status_code}]"
        logging.error(error_message)
        raise Exception(error_message)

    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
        for chunk in response.iter_content(chunk_size=1024):
            if cancel_event.is_set():
                return ""
            if chunk:
                temp_pdf.write(chunk)
        temp_pdf_path = temp_pdf.name

    pdf_content = ""
    with pdfplumber.open(temp_pdf_path) as pdf:
        for page in pdf.pages:
            if cancel_event.is_set():
                return ""
            page_text = page.extract_text()
            if page_text:
                pdf_content += page_text

    os.remove(temp_pdf_path)

    return pdf_content
