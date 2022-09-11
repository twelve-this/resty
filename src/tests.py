from dataclasses import dataclass

import pytest

from legacy.abstract_request import AbstractRequest

@dataclass
class DummyRequest(AbstractRequest):
    url = ""
    verb = ""
    params = {}
    headers = {}
    body = {}


@pytest.fixture
def request_obj_no_data():
    request = DummyRequest()
    return request


@pytest.fixture
def request_obj_simple_body(request_obj_no_data):
    # Simple body means, that body has only atomic values, e.g. string or int
    # not lists of dicts
    request_obj = request_obj_no_data

    request_obj.url = "my/test/url"
    request_obj.verb = "PUT"
    request_obj.params = {
        "param1": "param1_value",
        "param2": "param2_value",
    }
    request_obj.headers = {
        "header1": "header1_value",
        "header2": "header2_value",
        "header3": "header3_value",
    }
    request_obj.body = {}

    return request_obj


def test_request_obj_no_data(request_obj_no_data):
    request_obj = request_obj_no_data
    assert request_obj.url == ""
    assert request_obj.verb == ""
    assert request_obj.params == {}
    assert request_obj.headers == {}
    assert request_obj.body == {}

def test_request_obj_simple_body(request_obj_simple_body):
    request_obj = request_obj_simple_body
    assert request_obj == 55