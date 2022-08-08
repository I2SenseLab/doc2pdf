# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./


RUN apt-get update && \
	apt-get -y -q install \
		libreoffice \
		libreoffice-writer \
		ure \
		libreoffice-core \
		libreoffice-common \
		fonts-opensymbol && \
	apt-get -y -q remove libreoffice-gnome && \
	apt -y autoremove && \
	rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn --certfile MDAcert.pem --keyfile MDAkey.pem --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app