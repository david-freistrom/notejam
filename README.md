# Notejam (The first Cloud Based Deployment)

## The Cloud Enviornment

We decided to use GCP and it's Services only. 

* GCP Source Repository
* GCP Cloud Build
* GCP Cloud Run
* GCP Secret Manager
* GCP SQL
* GCP Artifact Registry


## Deployment and Release Strategy

There are 2 Environments (testing and production) and 2 permanent branches belongs to it.
Both have there own Database and are completly separate from each other.

Triggers for their CI/CD Pipelines are different.

For the testing branch, just a push into it triggers a complete build, test and deploy pipeline.
For the production branch a tagging is needed before it will deployed to the production environment.

There is also a developer trigger and pipeline without a own cloud based environment.
To run build and tests, a git push only is neeeded for each branch with a naming schmea like /^feature_.\*/


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
$ cloud-build-local --substitutions 'BRANCH_NAME=dev' --config=cloudbuild_dev.yaml --dryrun=false .
```

Build docker image locally
```bash
$ docker build notejam:dev .
```

Run the application in developer mode
```bash
$ FLASK_ENV=development flask run --host=0.0.0.0
```

