import pytest
from deeploy.parseRequest.service import ServiceParse

GITHUB = {
    'X-GITHUB-EVENT': 'merge',
    'X-GITHUB-DELIVERY': 'some_string',
    'X-HUB-SIGNATURE': 'another_string'
}

BITBUCKET = {
    'X-EVENT-KEY': 'some_string',
    'X-HOOK-UUID': 'some_UUID'
}

def test_github():
    service = ServiceParse(GITHUB).get_service()

    assert service == 'github'

def test_bitbucket():
    service = ServiceParse(BITBUCKET).get_service()

    assert service == 'bitbucket'

def test_none():
    service = ServiceParse({'x-no-service': 'header'}).get_service()

    assert service == None

def test_exception():
    with pytest.raises(Exception):
        ServiceParse({}).get_service()
