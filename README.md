## Developing

Install gcloud requirements for local builds ([Building and debugging locally][https://cloud.google.com/build/docs/build-debug-locally])

```bash
$ sudo yum install google-cloud-sdk-cloud-build-local
```

Run a local Ppostgresql Database
```bash
$ docker run -d --name postgres -e POSTGRES_USER=notejam -e POSTGRES_DB=notejam-db -e POSTGRES_PASSWWORD=password1234! -p 5432:5432 postgres:11
```

Create a new Branch from Masterpostgres
```bash
$ git checkout -b feature_x
```

Create a Virtual Environment
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

Build and test locally
```bash
$ cloud-build-local --config=cloudbuild_dev.yaml --dryrun=false .
```

Build docker image locally
```bash
$ docker build notejam:dev .
```

Run the application in developer mode
```bash
$ FLASK_ENV=development flask run --host=0.0.0.0
```

