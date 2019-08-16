class Github:
    def __init__(self, headers, payload):
        self.event = headers.get('X-GITHUB-EVENT')
        self.payload = payload

    def handle_pull_request(self, pull_request, scm='git'):
        '''  Extract project details from pull request '''

        pr = pull_request
        if self.event == 'pull_request' and pr['state'] == 'closed':

            return {
                'destination_branch': pr['base']['ref'],
                'respositor_name': pr['base']['repo']['full_name'],
                'repository_link': pr['base']['repo']['html_url'],
                'scm': scm,
                'git_url': {
                    'ssh': pr['base']['repo']['ssh_url'],
                    'https': pr['base']['repo']['clone_url']
                }
            }


    def parser(self):
        payload = self.payload
        # get pull request
        pr = payload.get('pull_request')

        if pr is not None:
            project_details = self.handle_pull_request(pr)

            print('payload', project_details)

            return project_details

        return False
