import pytest
from deeploy.parseRequest.bitbucket import Bitbucket
from .bitbucket_dummy_data import headers, pull_request

def test_parser():
    assert Bitbucket(headers, pull_request).parser(), "Test passed"
