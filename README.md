# kiko-slotfilling-example-python

In this example, user input data sent by an external Kiko sub-bot is processed.

## Setup Local Python Environment

Create and setup virtual environment
```
python -m venv env
source env/bin/activate
env/bin/pip install -U pip
env/bin/pip install -r requirements.txt
```

##  Run the Server Locally 

Activate the virtual environment, if necessary
```
source env/bin/activate
export FLASK_ENV=development
```

Run
```
FLASK_APP=main flask run
```
Check it out: http://127.0.0.1:5000/

## Expose your local service to the world

Open a new terminal and install nodejs, npm and localtunnel e.g. on macOS
```
brew install node
npm install -g localtunnel
```

Expose your local service port to your individual public https subdomain e.g. mydomain-kiko-slotfilling-example
```
lt --port 5000 --subdomain mydomain-kiko-slotfilling-example
```
Check it out and press "Click To Continue": https://mydomain-kiko-slotfilling-example.loca.lt/
...

## Webhook Url
You can use this url as endpoint for your "Nachricht erhalten" webhook in your Kiko External Subbot

Example webhook url: https://mydomain-kiko-slotfilling-example/api/v1/messages

# Related links
- [Set up slot filling in the Admin GUI](https://support.kiko.bot/portal/de/kb/articles/slot-filling-7-4-2021#Slot-Filling_Parameter_hinzufgen)
- [Data format from webhook](https://cloud02-7c83ec0.prod.1000grad.de/api/docs/#/webhooks?id=message_sent)
- [Data format for output messages](https://cloud02-7c83ec0.prod.1000grad.de/api/docs/#/message-types)