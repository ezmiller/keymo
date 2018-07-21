# Keymo

An experimental keyword extractor service.

To run as a docker service:

```
docker build -t keymo . && docker run -p 8080:8080 keymo
```

To run without docker using [pipenv]():

```
pipenv install
pipenv shell
FLASK_APP=api.py flask run &
```
