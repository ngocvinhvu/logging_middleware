import logging
from os import environ
from flask import current_app, request


def Logging():
    if 'FILENAME' in current_app.config:
        filename = current_app.config['FILENAME']
    else:
        filename = "request.log"
    return filename


def SolveReqHeader():
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
    return req


def SolveReqPayload():
    if isinstance(request.get_json(), dict):
        return request.get_json()
    else:
        for file in request.files.keys():
            blob = request.files[file].read()
            size = len(blob)
            if size < 20000:
                return blob
            else:
                return "File > 20000Kb"
    return None


def SolveResPayload(payload):
    keys = list(payload.keys())
    for key in keys:
        if key in current_app.config:
            if current_app.config[key] == False:
                del payload[key]

        elif isinstance(payload[key], dict):
            for key_1 in list(payload[key].keys()):
                if f'{key}/{key_1}' in current_app.config:
                    if current_app.config[f'{key}/{key_1}'] == False:
                        del payload[key][key_1]
                        payload.update({key: payload[key]})

                elif isinstance(payload[key][key_1], dict):
                    for key_2 in list(payload[key][key_1].keys()):
                        if f'{key}/{key_1}/{key_2}' in current_app.config:
                            if current_app.config[f'{key}/{key_1}/{key_2}'] == False:
                                del payload[key][key_1][key_2]
                                payload.update({key: payload[key]})
    return payload


def LoggingRequest():
    req_data = SolveReqPayload()
    req = SolveReqHeader()

    print('\nREQUEST header:\n{}'.format(req))
    print('\nREQUEST payload:\n{}\n'.format(req_data))

    if 'LOG_REQUEST' in current_app.config:
        if current_app.config['LOG_REQUEST']:
            filename = Logging()
            
            logging.basicConfig(
            filename=filename,
            level=logging.DEBUG,
            )
            logging.debug('\nREQUEST header:\n{}'.format(req))
            logging.debug('\nREQUEST payload:\n{}\n'.format(req_data))
    return None


def LoggingResponse(resp):
    header = resp.headers
    payload = resp.json
    print('\nRESPONSE header:\n{}'.format(header))
    
    if isinstance(payload, dict):
        res_payload = SolveResPayload(payload)
        print('\nRESPONSE payload:\n{}'.format(res_payload))

        if 'LOG_RESPONSE' in current_app.config:
            if current_app.config['LOG_RESPONSE']:
                filename = Logging()

                logging.basicConfig(
                filename=filename,
                level=logging.DEBUG,
                )
                logging.debug('\nRESPONSE header:\n{}'.format(header))
                logging.debug('\nRESPONSE payload:\n{}'.format(payload))
    else:
        print('RESPONSE payload:\n{}'.format(resp.get_data()))
        if 'LOG_RESPONSE' in current_app.config:
            if current_app.config['LOG_RESPONSE']:
                filename = Logging()

                logging.basicConfig(
                filename=filename,
                level=logging.DEBUG,
                )
                logging.debug('\nRESPONSE header:\n{}'.format(header))
                logging.debug('RESPONSE payload:\n{}'.format(resp.get_data()))
    return resp

