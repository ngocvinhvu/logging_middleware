import logging
from os import environ
from flask import current_app, request


def loggingrequest():
    fields = {}
    req = ''
    for field in request.headers.keys():
        fields.update({field: request.headers.get(field)})
        try:
            if current_app.config[field] == False:
                fields.pop(field)
        except KeyError:
            continue

    for field in fields.keys():
        request_header = '{}: {}\n'.format(field, fields[field])
        req += request_header
    print('REQUEST HEADER:\n{}'.format(req))

    print('\n{}\n'.format(request.get_json()))

    if current_app.config['LOG_REQUEST']:

        filename = "logging.log"
        logging.basicConfig(
            filename=filename,
            level=logging.DEBUG,
        )

        logging.debug('REQUEST HEADER:\n{}'.format(req))
        logging.debug('Request PayLoad: {}'.format(request.get_json()))


def loggingresponse(resp):
    header = resp.headers
    payload = resp.json
    print(header)
    
    if isinstance(payload, dict):
        payloads = {}
        keys = payload.keys()
        for key in keys:
            payloads.update({key: payload[key]})
            try:
                if current_app.config[key] == False:
                    payloads.pop(key)
            except KeyError:
                continue
        print(payloads)
    
        if current_app.config['LOG_RESPONSE']:
            logging.debug('Response header: {}'.format(header))
            logging.debug('Response payload: {}'.format(payloads))

    else:
        print(resp.get_data())

    return resp

