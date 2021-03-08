from flask import Flask, request
from flask.json import jsonify
from LoggingMiddleware import loggingrequest, loggingresponse

app = Flask(__name__)


app.before_request(loggingrequest)
app.after_request(loggingresponse)

app.config["TESTING"] = True

app.config["LOG_REQUEST"] = True

@app.route('/get', methods=['GET'])
def get():
    with open ('logging.log', 'r') as f:
        data = f.read()
    return jsonify({1: data})


if __name__ == "__main__":
    app.run()


# def create_app():
#     app = Flask(__name__)

#     #main
#     app.before_request(loggingrequest)
#     app.after_request(loggingresponse)

#     app.config["TESTING"] = True

#     app.config["LOG_REQUEST"] = True

#     with open (logging.log, 'r') as f:
#         data = f.read()

#     @app.route('/get', methods=['GET'])
#     def get():
#         return jsonify({1: data})

#     return app

# if __name__ == "__main__":
#     app = create_app()
#     app.run()