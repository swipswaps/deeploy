import pytest
from deeploy.parseRequest.bitbucket import Bitbucket
from .bitbucket_dummy_data import headers, pull_request

def test_parser():
    c = Bitbucket(headers, pull_request).parser()
    assert c, "Test passed"
    assert isinstance(c, dict), "Type dictionary"

def test_handle_request():
    pr = pull_request.get('pullrequest')
    scm = pull_request['repository']['scm']
    project_details = Bitbucket(headers, pull_request).handle_pull_request(pr, scm)
    assert isinstance(project_details, (dict)), "Return value is type dict"
