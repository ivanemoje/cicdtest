# FROM ubuntu:22.04

# RUN apt-get update
# RUN apt-get upgrade -y
# RUN apt-get install -y python3 python3-pip

# ENV DEBIAN_FRONTEND noninteractive
# RUN apt-get update && \
#     apt-get -y install gcc mono-mcs && \
#     rm -rf /var/lib/apt/lists/*

# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# # python packages
# RUN pip install --upgrade pip
    
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./application /application
WORKDIR /application/

ENV PYTHONPATH=/application

COPY models/boston_housting.onnx /tmp/boston_housing.onnx
ENV MODEL_PATH=/tmp/boston_housing.onnx

EXPOSE 80