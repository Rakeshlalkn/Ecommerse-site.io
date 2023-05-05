# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install --upgrade pip
RUN python -m pip install Pillow
RUN python -m pip install numpy
RUN pip install -r requirements.txt
COPY . /code/