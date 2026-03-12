FROM python:3.10-slim AS builder

WORKDIR /install

COPY requirements-api.txt .

RUN pip install --prefix=/install --no-cache-dir -r requirements-api.txt

FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY src ./src
COPY artifacts ./artifacts

EXPOSE 8000

CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000"]
