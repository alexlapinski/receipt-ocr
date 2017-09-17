FROM python:3

# TODO: Install / Compile Tesseract 4.0

# Install pipenv
RUN pip install pipenv

WORKDIR /usr/src/app

COPY Pipfile ./
RUN pipenv install

COPY ./src/ .

CMD [ "python", "./main.py" ]