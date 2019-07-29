'''
    Determines the service sending the request using the content of the
    request headers
 '''

class Service_parse:

    def __init__(self, request):
        self.headers = request.headers

    def get_service(self):
        '''
            get_service() -> string

            Return the name service making the request
        '''
        headers = self.headers
        if not headers:
            return

        '''
            github = ['X-GitHub-Event', X-GitHub-Delivery', 'X-Hub-Signature']
            bitbucket = ['X-Event-Key', 'X-Hook-UUID', 'X-Request-UUID', 'X-Attempt-Number']

            todo - gitlab, circleCI, travisCI
        '''
        if 'X-GitHub-Event' in headers and 'X-GitHub-Delivery' in headers and 'X-Hub-Signature' in headers:
            return 'github'
        elif 'X-Event-Key' in headers and 'X-Hook-UUID' in headers:
            return 'bitbucket'
