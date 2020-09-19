FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

RUN add-apt-repository ppa:ubuntugis/ppa && apt-get update && apt-get install -y gdal-bin python-gdal python3-gdal

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/