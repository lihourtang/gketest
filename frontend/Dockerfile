FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

ENV PYTHONUNBUFFERED True

ADD requirements.txt /
RUN pip install -r /requirements.txt
RUN pip install Flask gunicorn

ADD . /app
WORKDIR /app

# start flask app using Gunicorn
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 600 app:app
EXPOSE 80
CMD python app.py

