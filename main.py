from flask import Flask, request, send_file, Response, render_template, abort

app = Flask(__name__)


@app.route("/hello", methods=['GET'])
def hello():
    return "OK"


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=19888)
