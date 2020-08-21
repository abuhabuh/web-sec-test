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

Execution
1. Login as Alice to the bank server (localhost:5002/login). Just type "alice" 
and submit.
1. Observe Alice has X money.
1. Login as Chuck and observe Chuck has less money.
1. Load the attack page with dev console open and observe POST request sent (
but failed due to SOP)
1. Notice that Chuck's balance has not changed because the attack request (
transfer $ from Alice to Chuck) was not authorized since logged in user is 
Chuck
1. Login again as Alice
1. Load attack page and observe POST request sent
1. Observe Alice has less money
1. Login as Chuck and observe Chuck has more money. Winning.

