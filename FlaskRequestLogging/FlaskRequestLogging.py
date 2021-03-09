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
    print('\nREQUEST header:\n{}'.format(req))
    print('\nREQUEST payload:\n{}\n'.format(request.get_json()))

    if 'LOG_REQUEST' in current_app.config:
        if current_app.config['LOG_REQUEST']:
            if 'FILENAME' in current_app.config:
                filename = current_app.config['FILENAME']
            else:
                filename = "request.log"
            
            logging.basicConfig(
            filename=filename,
            level=logging.DEBUG,
            )
            logging.debug('\nREQUEST header:\n{}'.format(req))
            logging.debug('\nREQUEST payload:\n{}\n'.format(request.get_json()))


def loggingresponse(resp):
    header = resp.headers
    payload = resp.json
    print('\nRESPONSE header:\n{}'.format(header))
    
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
        print('\nRESPONSE payload:\n{}'.format(payloads))

        if 'LOG_RESPONSE' in current_app.config:
            if current_app.config['LOG_RESPONSE']:
                filename = "logging.log"
                logging.basicConfig(
                filename=filename,
                level=logging.DEBUG,
                )
                logging.debug('\nRESPONSE header:\n{}'.format(header))
                logging.debug('\nRESPONSE payload:\n{}'.format(payloads))
    else:
        print('RESPONSE payload:\n{}'.format(resp.get_data()))
        if 'LOG_RESPONSE' in current_app.config:
            if current_app.config['LOG_RESPONSE']:
                filename = "logging.log"
                logging.basicConfig(
                filename=filename,
                level=logging.DEBUG,
                )
                logging.debug('\nRESPONSE header:\n{}'.format(header))
                logging.debug('RESPONSE payload:\n{}'.format(resp.get_data()))

    return resp
