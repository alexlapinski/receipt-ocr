FROM python:3-stretch

# Install Dependencies for tesseract
RUN apt-get update && apt-get install -y \
    g++ \
    autoconf \
    automake \
    libtool \
    autoconf-archive \
    pkg-config \
    libpng-dev \
    libjpeg62-turbo-dev \
    libtiff5-dev zlib1g-dev \
    libleptonica-dev
RUN wget https://github.com/tesseract-ocr/tesseract/archive/4.00.00dev.tar.gz && tar xvf 4.00.00dev.tar.gz

# TODO: Make / Install tesseract 4.x
WORKDIR tesseract-4.00.00dev/
RUN ./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    ldconfig

# Install pipenv
RUN pip install pipenv

WORKDIR /usr/src/app

COPY Pipfile ./
RUN pipenv install

COPY ./src/ .

CMD [ "python", "./main.py" ]