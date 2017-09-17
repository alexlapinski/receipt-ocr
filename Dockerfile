FROM python:3

# Install pipenv
RUN pip install pipenv

WORKDIR /usr/scr/app

COPY Pipfile