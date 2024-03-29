# Features

- Default config show all of header and payload of request and response
- Optional hiding any field in header's request
- Optional hiding any field in payload's response if type of payload is JSON.
- Optional logging all infomation to optional filename, default name is "request.log"

# User Guide

- Create a virtual environtment: 
```
python3 -m venv venv
```
- Access to virtual environtment: 
```
source venv/bin/activate
```
- Install Flask: 
```
pip install flask
```
- Install Logging Middleware: 
```
pip install FlaskRequestLogging==0.1
```
- Add to your app (app.py):
```
from FlaskRequestLogging import LoggingRequest, LoggingResponse

app = Flask(...)

app.before_request(LoggingRequest)
app.after_request(LoggingResponse)

"your config position"

@app.route('/')...
```
# How to Config:
## NOTE:
## Default Config will show all of infomation in command line but not logging to file. 
### - Config field Request header:

#### Add 
```
app.config['field name'] = False
``` 
to "your config position" to hide that field.
#### Example
```
app.config['Cookie'] = False
```
 ===> field "Cookie" won't be shown.

### - Config log data of Request Payload:
#### Add 
```
"app.config['LOG_UPLOAD_LIMIT']" = "size of your file which you want to control the limit"
```
#### Example 
```
app.config['LOG_UPLOAD_LIMIT'] = 1000000
```
this means the contents of file > 1000000 Kb won't log to file.


### - Config field Response payload:

If your response data is Json, you could hide optional field. 
Currently, we provide this feature for hide the field at 3 level.
#### Example:
Response Payload: 
```
{"account": {
                "email": "test@example.com",
                "password": {
                            "value": "112233",
                            "type": "string"}
                        }
            }
```
#### - If you need to hide field in level 1:
#### Add 
```
app.config['key level 1'] = False
``` 
to "your config location" to hide that field.
#### Example: 
```
app.config['account'] = False
``` 
===> key and value of 'account' won't be shown.

#### - If you need to hide field in level 2:
#### Add 
```
app.config['key level 1/key level 2'] = False
``` 
to "your config location" to hide that field.
#### Example 
```
app.config['account/password'] = False
``` 
===> key and value of 'password' won't be shown.

#### - If you need to hide field in level 3:
#### Add 
```
"app.config['key level 1/key level 2/key level 3'] = False"
``` 
to "your config location" to hide that field.
#### Example: 
```
app.config['account/password/value'] = False 
```
===> key and value of 'value' won't be shown.



# Config to logging to file:

#### Add 
```
app.config['LOG_REQUEST'] = True
```
to "your config location" to add info of Request

#### Add 
```
app.config['LOG_RESPONSE'] = True
```
to "your config location" to add info of Response

#### Add
```
app.config['FILENAME']" = "your file name"
```
default file name: "request.log". 
 All infomation will be log to "your file name"
