FROM ubuntu:latest
MAINTAINER Pascal van Dam "pascal@poortier.nl"
RUN apt-get update -y && apt-get install -y python-pip python-dev build-essential curl
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
HEALTHCHECK CMD curl --fail http://localhost:5000/health || exit 1
ENTRYPOINT ["python"]
CMD ["example_app.py"]
