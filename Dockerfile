# syntax=docker/dockerfile:1
FROM python:3.4-alpine
RUN apk add curl
WORKDIR /code
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY app.py .
ENTRYPOINT ["python3"]
CMD ["app.py"]