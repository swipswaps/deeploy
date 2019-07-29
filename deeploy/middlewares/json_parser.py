
'''
Intercepts all request and response body with JSON document
'''

import json
import falcon

class Json_parser:

    def process_request(self, request, response):
        if request.content_length in (None, 0):
            return

        body = request.stream.read()

        if not body:
            raise falcon.HTTPBadRequest(
                'Empty request body. A valid JSON document is required.'
            )

        try:
            request.context.request = json.loads(body.decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(
                falcon.HTTP_753,
                'Malformed JSON payload. Could not decode the request body.'
            )


    def process_response(self, request, response):
        if 'response' not in response.context:
            return

        response.body = json.dumps(
            response.context.response, ensure_ascii = False
        )
