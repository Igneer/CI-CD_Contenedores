FROM python:3.12-slim

WORKDIR /app

COPY src/libraries.txt .

RUN pip install --no-cache-dir -r libraries.txt

COPY src/ .

CMD ["python"]