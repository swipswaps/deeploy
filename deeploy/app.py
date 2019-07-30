import falcon;
from .middlewares import Json_parser
from .handle_request import HandleRequest

API = application = falcon.API()

API.add_route('/', HandleRequest())
