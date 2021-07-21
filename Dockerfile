# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8080
RUN apt-get update && \
    apt-get install ca-certificates -y && \
    apt-get clean
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8080" ]