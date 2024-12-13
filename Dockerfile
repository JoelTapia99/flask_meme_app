FROM ubuntu:24.04
FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "index.py"]