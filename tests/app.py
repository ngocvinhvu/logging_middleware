from flask import Flask, request
from flask.json import jsonify
from LoggingMiddleware import loggingrequest, loggingresponse


def create_app():
    app = Flask(__name__)

    #main
    app.before_request(loggingrequest)
    app.after_request(loggingresponse)

    app.config["TESTING"] = True

    app.config["LOG_REQUEST"] = True

    app.config["Host"] = False

    app.config["Cookie"] = False

    app.config["LOG_RESPONSE"] = True

    @app.route('/get', methods=['GET'])
    def get():
        return jsonify({1: "hello"})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()