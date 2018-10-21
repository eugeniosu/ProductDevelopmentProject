FROM python:3.6

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/app

ADD requirements/requirementsDev.txt /usr/app/
RUN pip install -r requirementsDev.txt

