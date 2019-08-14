
import falcon
from .parseRequest.service import ServiceParse

class HandleRequest(object):
    def on_get(self, request, response):
        response.status = falcon.HTTP_404

    def on_post(self, request, response):
        service = ServiceParse(request.headers).get_service()
        if service is None:
            raise falcon.HTTPInvalidHeader('Could not identify the service send this request.', 'SERVICE')

        response.body = service
