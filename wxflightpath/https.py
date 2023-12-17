import logging

from wxflightpath.lambda_handler import *
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

# Define a route that accepts parameters in the URL
@app.route('/brief', methods=['GET'])
def brief():
    # Extract parameters from the query string
    origin = request.args.get('origin', 'LFRU')
    destination = request.args.get('destination', 'LFRU')
    event = {'flightpath': [origin, destination]}
    response_data = lambda_handler(event=event, context={})
    logging.info("Fligtpath %s --> %s", origin, destination)
    # Return a JSON response with a 200 OK status
    return jsonify(response_data['body']), 200
@app.route('/brief-redirect', methods=['GET'])
def briefRedirect():
    # Extract parameters from the query string
    origin = request.args.get('origin', 'LFRU')
    destination = request.args.get('destination', 'LFRU')
    event = {'flightpath': [origin, destination]}
    logging.info("Fligtpath %s --> %s",origin,destination)
    response_data = lambda_handler(event=event, context={})
    # Return a redirect
    return redirect(response_data['headers']['BriefingURL'], code=302)

if __name__ == '__main__':
    app.run(debug=True, port=8443, ssl_context=(config['HTTPS']['CERTPATH'], config['HTTPS']['KEYPATH']))
