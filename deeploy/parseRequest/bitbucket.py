class Bitbucket:
    def __init__(self, headers, payload):
        self.event_key = headers.get('X-EVENT-KEY')
        self.payload = payload

    def handle_pull_request(self, pull_request, scm):
        '''  Extract project details from pull request '''

        pr = pull_request
        if self.event_key == 'pullrequest:fulfilled' and pr['state'] == 'MERGED':

            return {
                'destination_branch': pr['destination']['branch']['name'],
                'respositor_name': pr['destination']['repository']['full_name'],
                'repository_link': pr['destination']['repository']['links']['html']['href'],
                'scm': scm,
                'git_url': {
                    'ssh': '',
                    'https': ''
                }
            }


    def parser(self):
        payload = self.payload
        # get pull request
        pr = payload.get('pullrequest')

        if pr is not None:
            project_details = self.handle_pull_request(pr, payload['repository']['scm'])

            print('payload', project_details)

            return project_details

        return False
