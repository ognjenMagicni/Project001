FROM python:3.12.0b1-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y pkg-config python3-dev default-libmysqlclient-dev build-essential default-libmysqlclient-dev
RUN pip3 install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]