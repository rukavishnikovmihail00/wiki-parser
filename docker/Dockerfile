FROM python:3.7-alpine3.15

WORKDIR /app

COPY . .

RUN pip install --upgrade pip Wikipedia-API backoff

RUN chmod +x start.sh

ENTRYPOINT ["./start.sh"]