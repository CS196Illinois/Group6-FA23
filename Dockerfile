FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

ADD . /code/

EXPOSE 8000

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "./Project/stocks/manage.py", "runserver", "0.0.0.0:8000"]