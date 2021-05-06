FROM python:3-alpine
MAINTAINER pascal@k8s4all.com

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /app

# Expose the Flask port
EXPOSE 8080

CMD [ "python", "./pyco2.py" ]
