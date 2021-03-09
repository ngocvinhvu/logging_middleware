# Features

- Default config show all of header and payload of request and response
- Optional hiding any field in header's request
- Optional hiding any field in payload's response if type of payload is JSON.
- Optional logging all infomation to filename logging.log

# User Guide

- Create a virtual environtment: python3 -m venv venv
- Access to virtual environtment: source venv/bin/activate
- Install Flask: pip install flask
- Install Logging Middleware: pip install git+https://github.com/ngocvinhvu/logging_middleware.git#egg=LoggingMiddleware
- Add to your app (app.py):

- from LoggingMiddleware import loggingrequest, loggingresponse
- app = Flask(...)
- app.before_request(loggingrequest)
- app.after_request(loggingresponse)
- #yourconfig
- @app.route('/')...

# How to Config:
- Default Config will show all of infomations in command line but not logging to file. 
- Config field Request header:

Add "app.config['field name'] = False" to #yourconfig to hide that field.
Exp: app.config['Cookie'] = False ===> field "Cookie" won't be shown.

- Config field Response payload:

Add "app.config['field name'] = False" to #yourconfig to hide that field
Exp: app.config['id'] = False ===> key "id" won't be shown.

- Config to logging to file (logging.log):

Add "app.config['LOG_REQUEST'] = True" to #yourconfig to add info of Request

Add "app.config['LOG_RESPONSE'] = True" to #yourconfig to add info of Response

All infomation will log to filename logging.log
