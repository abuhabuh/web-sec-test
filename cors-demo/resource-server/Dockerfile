FROM frolvlad/alpine-python3

RUN mkdir -p /var/www/server/
COPY resource-server/ /var/www/server/resource_server/

RUN pip install -r /var/www/server/resource_server/requirements.txt

ENTRYPOINT ["python", "/var/www/server/resource_server/server.py"]

