# Overview

Base server and client applications to copy and build demos with

# Running

1. build images: `docker-compose build`
2. from the base run `docker-compose up -d`
3. navigate to either localhost:5001 (client UI) or localhost:5002 (server UI)

# Details

Two servers boot up (see docker-compose.yml):

* client-server
  * origin: localhost:5001

* resource-server
  * origin: localhost:5002

