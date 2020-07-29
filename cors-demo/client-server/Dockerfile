FROM frolvlad/alpine-python3

RUN mkdir -p /var/www/server/client-server
COPY client-server /var/www/server/client-server

RUN pip install -r /var/www/server/client-server/requirements.txt

### Prepare and run the server
# Set working dir to exec flask run
WORKDIR /var/www/server/
# Set env var for running server
ENV PYTHONPATH=/var/www/server/client-server
ENV FLASK_APP=client-server/app:app
ENTRYPOINT ["flask", "run", "--port", "5001", "--host", "0.0.0.0", "--reload"]

