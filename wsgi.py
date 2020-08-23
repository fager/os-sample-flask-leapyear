import calendar
from flask import Flask, jsonify
import socket


application = Flask(__name__)

@application.route("/")
def hello():
    return "API: /leapyear/<int>"

@application.route("/healthz")
def healthz():
    return "OK"

@application.route("/leapyear/<int:i_year>")
def leapyear( i_year ):
    ret_leap = calendar.isleap(i_year)
    ret_hostname = socket.gethostname()

    return jsonify( { 'isleapyear': ret_leap, 'worker': ret_hostname } )

if __name__ == "__main__":
    application.run()
