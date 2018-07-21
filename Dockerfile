FROM python:3.6

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /app

WORKDIR /app

CMD ["gunicorn", "-b :8080", "api:app"]
