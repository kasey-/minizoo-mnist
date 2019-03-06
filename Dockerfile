FROM python:3.6

COPY ./mnist /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "gunicorn", "--workers=2", "-b 0.0.0.0:80", "--timeout=120", "main:app" ]