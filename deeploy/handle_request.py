import json
import falcon
from .parseRequest.service import ServiceParse

class HandleRequest(object):
    def on_get(self, request, response):
        ''' Handle GET request '''
        response.status = falcon.HTTP_404

    def on_post(self, request, response):
        ''' Handles post request '''

        # check content length
        if request.content_length in (None, 0):
            raise falcon.HTTPBadRequest('Bad request',
                                        'Make a valid request with the request parameter')

        body = request.stream.read(request.content_length or 0)
        if not body:
            raise falcon.HTTPBadRequest('Empty request sent', 'A valid JSON document is required.')

        try:
            body = json.loads(body.decode('utf-8'))
            # Determine the service and dispatch request
            ServiceParse(request.headers).request_dispatcher(body)

        except UnicodeDecodeError:
            raise falcon.HTTPError(falcon.HTTP_753, 'Malformed JSON',
                                   'Could not decode the request body.')
