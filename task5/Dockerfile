FROM python:3.10-slim

WORKDIR /app

COPY postgre.py .

RUN pip install --no-cache-dir psycopg2-binary

CMD ["python", "postgre.py"]