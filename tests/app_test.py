from flask import Flask, request
from flask.json import jsonify
from FlaskRequestLogging import LoggingRequest, LoggingResponse


def create_app():
    app = Flask(__name__) 

    #main
    app.before_request(LoggingRequest)
    app.after_request(LoggingResponse)

    app.config["TESTING"] = True

    app.config["LOG_REQUEST"] = True

    app.config["LOG_RESPONSE"] = True

    app.config["Host"] = False

    app.config["Cookie"] = False

    app.config["LOG_RESPONSE"] = True

    app.config["FILENAME"] = "request1.log"

    app.config["account/password/value"] = False

    app.config['LOG_UPLOAD_LIMIT'] = 12345


    @app.route('/get', methods=['GET'])
    def get():
        return jsonify({"account": {
                            "email": "test@example.com",
                            "password": {
                                "value": "112233",
                                "type": "string"}
                                    }})

    @app.route('/post', methods=['GET', 'POST'])
    def post():
        return jsonify({1: str(request.data)})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)