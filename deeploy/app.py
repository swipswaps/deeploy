import falcon;

from .middlewares import Json_parser

API = application = falcon.API(middlewares=[
    Json_parser()
])
