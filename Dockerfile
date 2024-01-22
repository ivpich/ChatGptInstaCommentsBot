FROM --platform=linux/amd64 python:3.8-slim-buster

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "./main.py"]