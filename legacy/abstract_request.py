from dataclasses import dataclass, field
from typing import Any


import requests

@dataclass
class AbstractRequest:

    url: str = field(init=False)
    verb: str = field(init=False)
    params: dict[str, str] = field(init=False, default_factory=dict)
    headers: dict[str, str] = field(init=False, default_factory=dict)
    body: dict[str, Any] = field(init=False, default_factory=dict)

    def fire_request(self) -> None:

        r = requests.request(method=self.verb, url=self.url, headers=self.headers, params=self.params, data=self.body)



@dataclass
class AbstractJiraRequestWithFields(AbstractRequest):

    url = "asdfasdf"
    verb = "POST"
    params = None
    headers = {
        "header1": "header1_value",
        "header2": "header2_value",
        "header3": "header3_value",
    }

    body = {}



class RequestObject:

    def __init__(self):
        self.url = None
        self.verb = None
        self.body = None


    def set_url(self, url):
        self.url = url
        return self

    def set_verb(self, verb):
        self.verb = verb
        return self

    def set_body(self, body):
        self.body = body
        return self

    def fire_request(self):
        r = requests.request(method=self.verb, url=self.url, headers=self.headers, params=self.params, data=self.body)


url = "to/my/favority/endpoint"
verb = "PUT"
body = {
    "key": "value",
    "key1": [],
}

ro = RequestObject().set_url(url).set_verb(verb).set_body(body).fire_request()



class SomeService:

    def fire_request(self):
        pass

    def getTests(self, body):
        r = requests.request(
            method=self.verb,
            url=self.url,
            headers=self.headers, params=self.params, data=self.body)

    def get_test_executions(self, body):
        url = "/my/url"
        verb = "GET"
        headers = 6
