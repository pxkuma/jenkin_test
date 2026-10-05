# Zero-touch CI/CD on AWS (sample service)

A small Python service used to exercise a fully automated Jenkins pipeline. Every merge to `main` is built, tested, quality-gated and deployed without anyone logging into a server.

## Pipeline

1. **Trigger:** a GitHub webhook starts the Jenkins job on every merge to `main`.
2. **Build and test:** a declarative Jenkinsfile runs short-lived Node.js and Python Docker agents that install dependencies and run the unit tests.
3. **Quality gate:** SonarQube static analysis has to pass before anything ships.
4. **Deploy:** Jenkins connects to the production host over SSH and rebuilds the containers with Docker Compose.

Jenkins, SonarQube and the deployment target each run on their own AWS EC2 instance, so a broken build can never take production down with it.

## Run the tests locally

```bash
pip install -r requirements.txt
python -m pytest
```

## Repository contents

| File | Purpose |
| --- | --- |
| `app.py` | Service logic under test |
| `test_app.py` | Unit tests the pipeline runs on every build |
| `requirements.txt` | Test dependencies |
