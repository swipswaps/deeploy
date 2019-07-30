import sys
sys.path.append('..')
import falcon
from falcon import testing
import pytest
from deeploy.app import API

@pytest.fixture
def client():
    return testing.TestClient(API)

def test_send_post(client):
    response = client.simulate_post('/')

    assert response.status == falcon.HTTP_OK
