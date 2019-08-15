''' Returns the name of the service sending the request '''

from .bitbucket import Bitbucket
class ServiceParse:
    '''
        ServiceParse()
        Example:
        ServiceParse({}).get_service() -> string

        Determines the service sending the request using the content
        of the request headers
    '''

    def __init__(self, headers):
        self.headers = headers

    def get_service(self):
        '''
            get_service() -> string

            Return the name of service making the request
        '''
        headers = self.headers
        if not headers:
            raise Exception('Invalid request.')

        # github = ['X-GitHub-Event', X-GitHub-Delivery', 'X-Hub-Signature']
        if (
                ('X-GITHUB-EVENT' in headers) and
                ('X-GITHUB-DELIVERY' in headers) and
                ('X-HUB-SIGNATURE' in headers)
            ):
            return 'github'

        # bitbucket = ['X-Event-Key', 'X-Hook-UUID', 'X-Request-UUID', 'X-Attempt-Number']
        if (('X-EVENT-KEY' in headers) and ('X-HOOK-UUID' in headers)):
            return 'bitbucket'

        # (todo - gitlab, circleCI, travisCI)
        return None

    def request_dispatcher(self, payload):
        service = self.get_service()

        if service is None:
            raise Exception('Could not identify the service that sent this request.')

        if service == 'bitbucket':
            # handle
            Bitbucket(self.headers, payload).parser()

            return service

        # (todo - remove)
        return service

