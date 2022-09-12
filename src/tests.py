from dataclasses import dataclass

import pytest

from src.api_spec import APISpec
from src.endpoint import Endpoint
from src.main import load_api_spec


@pytest.fixture
def global_headers_raw():
    return {
        "header1": "header1_value",
        "header2": "header2_value",
        "header3": "header3_value",
    }


@pytest.fixture
def endpoints_raw():
    return {
        "get_issue_by_key": {
            "url": "/rest/api/2/issue/{key}",
            "verb": "GET",
            "additional_headers": {},
            "remove_global_headers": [],
            "path_parameters": ["key"],
            "query_parameters": {},
        },
        "create_issue": {
            "url": "/rest/api/2/issue",
            "verb": "POST",
            "additional_headers": {
                "header2": "header2_value_overridden",
                "header4": "header4_value",
            },
            "remove_global_headers": ["header3"],
            "path_parameters": [],
            "query_parameters": {},
        },
    }


@pytest.fixture
def endpoints_as_obj():
    return {
        "get_issue_by_key": Endpoint(
            name="get_issue_by_key",
            url="/rest/api/2/issue/{key}",
            verb="GET",
            global_headers={
                "header1": "header1_value",
                "header2": "header2_value",
                "header3": "header3_value",
            },
            additional_headers={},
            remove_global_headers=[],
            path_parameters=["key"],
            query_parameters={},
        ),
        "create_issue": Endpoint(
            name="create_issue",
            url="/rest/api/2/issue",
            verb="POST",
            global_headers={
                "header1": "header1_value",
                "header2": "header2_value",
                "header3": "header3_value",
            },
            additional_headers={
                "header2": "header2_value_overridden",
                "header4": "header4_value",
            },
            remove_global_headers=['header3'],
            path_parameters=[],
            query_parameters={},
        ),
    }

@pytest.fixture
def headers_overridden():
    return {
        "header1": "header1_value",
        "header2": "header2_value_overridden",
        #"header3": "header3_value",
        "header4": "header4_value",
    }




@pytest.fixture
def jira_api_spec_no_yaml(global_headers_raw, endpoints_raw):
    name = "FakeJiraAPISpec"
    api_spec = APISpec(
        name=name, global_headers=global_headers_raw, endpoints_raw=endpoints_raw
    )
    return api_spec


@pytest.fixture
def jira_api_spec():
    path_jira_api_spec = "jira_api_specification.yaml"
    return load_api_spec("JiraAPI", path_jira_api_spec)


def test_jira_api_no_yaml(
    jira_api_spec_no_yaml, global_headers_raw, endpoints_raw, endpoints_as_obj
):
    api_spec = jira_api_spec_no_yaml

    assert api_spec.global_headers == global_headers_raw
    assert api_spec.endpoints_raw == endpoints_raw
    assert api_spec.endpoints == endpoints_as_obj


def test_api_spec_endpoint_headers_overridden(jira_api_spec_no_yaml, headers_overridden, global_headers_raw):

    create_issue = jira_api_spec_no_yaml.get_endpoint("create_issue")
    assert create_issue.headers == headers_overridden

    get_issue_by_key = jira_api_spec_no_yaml.get_endpoint("get_issue_by_key")
    assert get_issue_by_key.headers == global_headers_raw

def test_api_spec_endpoint_ready_url(jira_api_spec_no_yaml):

    create_issue = jira_api_spec_no_yaml.get_endpoint("create_issue")
    assert create_issue.has_path_parameters_in_url is False
    assert create_issue.path_parameters_provided is False
    assert create_issue._actual_path_parameters == {}

    get_issue_by_key = jira_api_spec_no_yaml.get_endpoint("get_issue_by_key")
    assert get_issue_by_key.has_path_parameters_in_url is True
    assert get_issue_by_key._actual_path_parameters == {}
    assert get_issue_by_key.path_parameters_provided is False

    path_parameters = {"key": "ISSUE-1234"}

    get_issue_by_key.provide_path_parameters(path_parameters)
    assert get_issue_by_key._actual_path_parameters == path_parameters
    assert create_issue._actual_path_parameters == {}

# @pytest.mark.skip
# def test_jira_api_spec(jira_api_spec):
#     assert jira_api_spec.global_headers == {
#         "header1": "header1_value",
#         "header2": "header2_value",
#         "header3": "header3_value",
#     }
#
#     endpoints = {
#         "get_issue_by_key": Endpoint(
#             name="get_issue_by_key",
#             url="/rest/api/2/issue/{key}",
#             verb="GET",
#             global_headers={
#                 "header1": "header1_value",
#                 "header2": "header2_value",
#                 "header3": "header3_value",
#             },
#             additional_headers={},
#             remove_global_headers={},
#             path_parameters={},
#             query_parameters={},
#         ),
#         "create_issue": Endpoint(
#             name="create_issue",
#             url="/rest/api/2/issue",
#             verb="POST",
#             global_headers={
#                 "header1": "header1_value",
#                 "header2": "header2_value",
#                 "header3": "header3_value",
#             },
#             additional_headers={
#                 "header2": "header2_value_overridden",
#                 "header4": "header4_value",
#             },
#             remove_global_headers={},
#             path_parameters={},
#             query_parameters={},
#         ),
#     }
#
#     assert jira_api_spec.endpoints == endpoints
#
#     endpoint = jira_api_spec.get_endpoint("create_issue")
#     assert endpoint.name == "create_issue"
#
#     headers_property = {
#         "header1": "header1_value",
#         "header2": "header2_value_overridden",
#         "header3": "header3_value",
#         "header4": "header4_value",
#     }
#
#     assert endpoint.headers == headers_property
