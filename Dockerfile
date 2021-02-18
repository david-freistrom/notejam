# Dockerfile
FROM python:3.7-stretch

ENV POSTGRES_USER=notejam
ENV POSTGRES_DB=notejam-db
ENV POSTGRES_PASSWORD=password1234!
ENV FLASK_ENV=production

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /workspace
WORKDIR /workspace
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["wsgi.py"]
