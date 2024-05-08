from flask import Flask, request, send_file, Response, render_template, abort

import pyotp

app = Flask(__name__)


@app.route("/hello", methods=['GET'])
def hello():
    return "OK"


@app.route("/otp", methods=['GET'])
def otp():
    totp = pyotp.TOTP('NSSQPXQGNJX7U6MW')
    return str(totp.now())


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=80)
