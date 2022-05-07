import json
from datetime import datetime
from flask import Flask, request, abort
from flask.logging import create_logger
from werkzeug.exceptions import HTTPException
import os
import requests

app = Flask(__name__)
app.logger = create_logger(app)

@app.route("/", methods=['GET'])
def health():
    return "ping"

@app.route("/api/v1/messages", methods=['POST'])
def api_v1_messages_post():
    body = request.get_json()
    messages = body.get('messages')
    metadata = messages[0].get('metaData')
    if metadata is None:
        abort(400, description="missing metadata in the first message")

    parameters = metadata.get('slotFillingParameter')
    if parameters is None:
        abort(400, description="missing slotFillingParameter in metaData")

    my_function(parameters)
    
    # --------------------------
    requests.post(url="https://" + ( request.args.get('callback-domain') or 'cloud02-7c83ec0.prod.1000grad.de') + "/api/api/v1/conversation/send", json={
        "conversationId": body.get('conversationId'),
        "messages": [
            {
                "type": "message",
                "data": {
                    "type": "text/plain",
                    "content": 'Vielen Dank. Ihre Daten werden verarbeitet.'
                }               
            },
            {
                "type": "event",
                "name": "endOfConversation"
            }
        ]
    })
    return {"success": True}

@app.errorhandler(HTTPException)
def handle_exception(err):
    response = err.get_response()
    response.data = json.dumps({
        "code": err.code,
        "name": err.name,
        "description": err.description,
    })
    response.content_type = "application/json"
    return response

def my_function(parameters):
  # do something with the parameters
  app.logger.info("parameter: {0}".format(parameters))
  return


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))