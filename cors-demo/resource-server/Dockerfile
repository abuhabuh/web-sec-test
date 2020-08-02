FROM frolvlad/alpine-python3

RUN mkdir -p /var/www/server/resource-server
COPY resource-server /var/www/server/resource-server
RUN pip install -r /var/www/server/resource-server/requirements.txt

### env setup to the server
WORKDIR /var/www/server/
ENV PYTHONPATH=/var/www/server/resource-server
ENV FLASK_APP=resource-server/server:app

ENTRYPOINT ["flask", "run", "--port", "5000", "--host", "0.0.0.0", "--reload"]

