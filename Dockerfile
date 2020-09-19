FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN apt-get update && apt-get install --yes libgdal-dev
RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
RUN export C_INCLUDE_PATH=/usr/include/gdal
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/