FROM alpine:3.2

# Install OS Dependencies
RUN apk update && apk add \
    ca-certificates \
    postgresql-dev \
    python-dev \
    build-base \
    && rm -rf /var/cache/apk/*

# Install pip
RUN wget https://bootstrap.pypa.io/get-pip.py -O - | python

# Ensure a SOON user exists
RUN adduser SOON -D

EXPOSE 8000

WORKDIR /app
COPY ./app/ /app

RUN pip install -r requirements.txt

CMD ["sh", "run.sh"]
