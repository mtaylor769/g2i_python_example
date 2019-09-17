import uuid
import g2i_test
import json
import pprint
# from sentry_sdk.integrations.flask import FlaskIntegration


import os
from flask import Flask, request, render_template, url_for, send_from_directory, logging, jsonify

strict_slashes=False

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TRAP_HTTP_EXCEPTIONS'] = True
app.config['TRAP_BAD_REQUEST_ERRORS'] = True

# the App Engine WSGI application server.
if __name__ == '__main__':
    app.secret_key = str(uuid.uuid4())
    app.debug = True
log = app.logger

@app.route('/')
def hello():
    error = None
    try:
        data = g2i_test.build_site_map('http://www.mozilla.com')
        return render_template('output.html', data=data)
    except KeyError as identifier:
        error = "FormError: " + identifier.message
        return render_template('error.html', error=error)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


