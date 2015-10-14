FROM debian:jessie

# Install OS Dependencies
RUN apt-get update && \
    apt-get install -y \
        libpq-dev \
        postgresql-client \
        python-dev \
        python-pip

# Ensure a SOON user exists
RUN useradd SOON

EXPOSE 8000

WORKDIR /app
COPY ./app/ /app

RUN pip install -r requirements.txt

CMD ["sh", "run.sh"]
