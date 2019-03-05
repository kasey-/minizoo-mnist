FROM continuumio/miniconda3

RUN conda install --yes tensorflow
RUN conda install --yes keras

COPY ./mnist /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "gunicorn", "--workers=2", "-b 0.0.0.0:80", "--timeout=120", "main:app" ]
