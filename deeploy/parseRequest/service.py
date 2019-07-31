''' Returns the name of the service sending the request '''
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

        service = None
        # github = ['X-GitHub-Event', X-GitHub-Delivery', 'X-Hub-Signature']
        if (
                ('X-GITHUB-EVENT' in headers) and
                ('X-GITHUB-DELIVERY' in headers) and
                ('X-HUB-SIGNATURE' in headers)
            ):
            service = 'github'

        # bitbucket = ['X-Event-Key', 'X-Hook-UUID', 'X-Request-UUID', 'X-Attempt-Number']
        if (('X-EVENT-KEY' in headers) and ('X-HOOK-UUID' in headers)):
            service = 'bitbucket'

        # (todo - gitlab, circleCI, travisCI)
        return service
