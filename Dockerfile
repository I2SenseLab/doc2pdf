# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

RUN apt update
RUN	apt -y -q install libreoffice
RUN	apt -y -q install libreoffice-writer
RUN apt -y -q install ure
RUN apt -y -q install libreoffice-core
RUN apt -y -q install libreoffice-common
RUN apt -y -q install fonts-opensymbol
RUN apt -y -q remove libreoffice-gnome
RUN apt -y autoremove
RUN	rm -rf /var/lib/apt/lists/*

RUN adduser --home=/opt/libreoffice --disabled-password --gecos "" --shell=/bin/bash libreoffice

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

EXPOSE 8080

# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt


# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app