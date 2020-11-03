from flask import Response, json

RESPONSES = {'INIT': 'Starting service',
             'BUSY': 'Service under execution',
             'ERR': 'Generic error received'}


class CustomResponse:
    response = Response(status=200, mimetype='application/json')
    response_body = {
        'msg': '',
        'status': '',
        'cache': {},  # Cache provided by service
    }

    def send_status(self, status: str, cache: dict):
        # Sanity check response from service
        if status not in RESPONSES:
            self.response_body['msg'] = 'Unknown Signal received from Service;'
            self.response_body['status'] = 'ERR'
            return self.response

        # Normal execution
        self.response_body['status'] = status
        self.response_body['cache'] = cache
        self.response_body['msg'] = RESPONSES[status]
        self.response.data = json.dumps(self.response_body)

        return self.response
