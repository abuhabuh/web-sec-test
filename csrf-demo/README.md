# Overview

Base server and client applications to copy and build demos with

# Running

1. build images: `docker-compose build`
2. from the base run `docker-compose up -d`
3. navigate to either localhost:5001 (client UI) or localhost:5002 (server UI)

# Details

Premise is that resource server holds bank acnt info.

## Scenario 1

* Resource server has two acnts (Alice and Chuck) with balances.
* Alice logs into her account via client server.
* Chuck tricks Alice into clicking a link that uses her login cookie to auth
  and transfer $ to his account.

