FROM python:3.11-slim AS builder

COPY ./src/requirements.txt .

RUN apt-get update && pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt


FROM gcr.io/distroless/python3-debian12:nonroot

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages:/app

COPY ./src /app/src

WORKDIR /app/src

ENTRYPOINT ["python", "app.py"]
