import pytest
from deeploy.parseRequest.service import ServiceParse

GITHUB = {
    'X-GitHub-Event': 'merge',
    'X-GitHub-Delivery': 'some_string',
    'X-Hub-Signature': 'another_string'
}

BITBUCKET = {
    'X-Event-Key': 'some_string',
    'X-Hook-UUID': 'some_UUID'
}

REQUEST = {
    'headers': {}
}

def test_github():
    REQUEST['headers'] = GITHUB
    service = ServiceParse(REQUEST).get_service()

    assert service == 'github'

def test_bitbucket():
    REQUEST['headers'] = BITBUCKET
    service = ServiceParse(REQUEST).get_service()

    assert service == 'bitbucket'

def test_none():
    REQUEST['headers'] = {'x-no-service': 'header'}
    service = ServiceParse(REQUEST).get_service()

    assert service == None

def test_exception():
    with pytest.raises(Exception):
        ServiceParse({}).get_service()
