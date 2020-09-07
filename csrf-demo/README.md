# Overview

Demonstration of CSRF attack on a server that tracks sessions in plain http
cookie.

# Running

1. build images: `docker-compose build`
2. from the base run `docker-compose up -d`
3. navigate to either localhost:5001 (client UI) or localhost:5002 (server UI)

# Details

Premise is that a resource server holds bank acnt info for two people: Alice
and Chuck. Chuck uses an evil client server to submit a CSRF attack that
transfers money from Alice's account to Chuck's account.

The CSRF attack relies on the fact that Alice is logged in and that her
session id is tracked in a simple http cookie. Chuck then gets Alice to visit
an attack page that sends a POST request to the resource server. Alice's http
session cookie is automatically sent with the POST request and authorizes the
transaction request.

## Scenario

* Resource server has two acnts (Alice and Chuck) with balances.
* Alice logs into her account via client server.
* Chuck tricks Alice into clicking a link that uses her login cookie to auth
  and transfer $ to his account.

Execution
1. Login as Alice to the bank server (localhost:5002/login). Just type "alice"
and submit.
1. Observe Alice has X money.
1. Login as Chuck and observe Chuck has less money (separate browser /
incognito)
1. Load the attack page (localhost:5001/attack) in Chuck's browser with dev
console open and observe POST request sent (but failed due to SOP)
1. Notice that Chuck's balance has not changed because the attack request (
transfer $ from Alice to Chuck) was not authorized since logged in user is 
Chuck
1. Login again as Alice
1. Load the attack page (localhost:5001/attack) in Alice's browser and observe
POST request sent
1. Observe Alice has less money
1. Login as Chuck and observe Chuck has more money. Winning.

