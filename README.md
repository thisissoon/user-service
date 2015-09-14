# User Service

User service is Django app for user management. App can create new users using
OAuth or through REST api resources.


## Environment variables

- `DATABASE_NAME`: database name (postgres)
- `DATABASE_USER`: database user (postgres)
- `DATABASE_PASSWORD`: database password (postgres)
- `DATABASE_HOST`: database host (database)
- `DATABASE_PORT`: database port (5432)


### Run

Run the project using a container:

```
docker run --rm -it soon/user-service:latest
```


### Development:

Example of fugu file. Once you build it you can run CMS by `fug run api`. CMS and API
should be accessible on your localdocker on `/admin` and `/api`.

``` yaml
=======
# User service

User service is Django app handles user authentication and authorization with
3rd party services i.e. Facebook, Google, Instagram and Twitter.

## Dev

Example of fugu.yaml file:

```yaml
base: &base
  image: soon/user-service:latest
  rm: true
  interactive: true
  tty: true
  link:
    - userservice_postgres_1:database
  env:
    - DATABASE_NAME=postgres
    - DATABASE_USER=postgres
    - DATABASE_PASSWORD=postgres
    - DATABASE_HOST=database
    - DATABASE_PORT=5432
    - DJANGO_SETTINGS_MODULE=userservice.settings.dev
  volume:
    - ../dev/user-service/app:/app/

api:
    <<: *base
    name: api
    publish:
      - 8000:8000

bash: &bash
    <<: *base
    name: user_bash
    command: /bin/sh
```

## Settings

App has several different settings:

- `base`: generic settings contains. Should not be used directly
- `dev`: simple settings using a temporary directory for storing media
- `qa`: same as development but uses AWS as storage - most similar to production
- `test`: used for unit testing


## Docs

You can run `make` to build a documentation. If you choose HTML documentation
the documentation should be in /docs/_build/html/index.html.

To generate new documentation rst files run `sphinx-apidoc -o docs/ app/`. You
have to install `napoleon` Sphinx extensions to generate Google style docs

```
pip install sphinxcontrib-napoleon
```

Sphinx requires some project dependencies for generate full documentation without
any warnings use the container and extend your `fugu.yaml`.

``` yaml
docs:
    <<: *bash
    name: docs
    volume:
      - .../dev/user-service:/app/
```
