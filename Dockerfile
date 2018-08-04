FROM tiangolo/uwsgi-nginx-flask:python3.6
COPY . /app
EXPOSE 8080
