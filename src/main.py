from pprint import pprint

import yaml

from src.api_spec import APISpec


def load_api_spec(name: str, path: str) -> APISpec:
    with open(path, "r") as stream:
        loaded_stream = yaml.safe_load(stream)
        global_headers = loaded_stream["global_headers"]
        endpoints = loaded_stream["endpoints"]
        return APISpec(
            name=name, global_headers=global_headers, endpoints_raw=endpoints
        )


def main():

    path_jira_api_spec = "jira_api_specification.yaml"
    jira_api_spec = load_api_spec("JiraAPI", path_jira_api_spec)

    pprint(jira_api_spec)
    print(jira_api_spec.endpoints_raw)


if __name__ == "__main__":
    main()
