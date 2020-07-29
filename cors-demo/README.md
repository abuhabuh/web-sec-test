# Overview

Sandbox and demo repo for testing CORS functionality

# Running

1. from the base `cors-demo/` directory, run `docker-compose up`
2. open up browser and display network tab
3. navigate to localhost:5001 and observe network requests and 
   responses
4. todo: fill out server info

# Details

Two servers boot up (see docker-compose.yml):

* client-server
  * origin: localhost:5001

* resource-server
  * origin: localhost:5002

CORS requests are sent from client-server to the resource-server.
Different CORS requests are sent (GET, POST, pre-flight) to 
demonstrate effects on the client and on the resource server. 

