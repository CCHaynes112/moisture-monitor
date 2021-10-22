FROM python:3

WORKDIR /app
COPY ./requirements.txt /app/

RUN pip install --upgrade --no-cache-dir pip==21.0.1
RUN pip install --no-cache-dir gunicorn==20.0.4
RUN pip install -r requirements.txt --no-cache-dir

COPY . /app/
WORKDIR /app/