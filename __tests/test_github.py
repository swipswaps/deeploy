import pytest
from deeploy.parseRequest.github import Github
from .github_dumy_data import pr_payload, headers

def test_parser():
    g = Github(headers, pr_payload).parser()
    assert g != False, 'Expect return value to be thruthy value'
    assert isinstance(g, dict), 'Expect return value to be of type dictionary'


def test_handle_request():
    pr = pr_payload.get('pull_request')
    g = Github(headers, pr_payload).handle_pull_request(pr)

    assert isinstance(g, dict), 'Expect return value to be type of dict'
