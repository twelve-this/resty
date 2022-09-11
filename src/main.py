import yaml

from src.endpoint_specs import APISpec
from src.endpoints import Endpoints


def load_api_spec(name: str, path: str) -> APISpec:
    with open(path, "r") as stream:
        loaded_stream = yaml.safe_load(stream)
        global_headers = loaded_stream["global_headers"]
        endpoints = loaded_stream["endpoints"]
        api_spec = APISpec(name=name, global_headers=global_headers, endpoints=endpoints)
        return Endpoints.load(name, api_spec)


# def load_endpoints(name: str, api_spec: APISpec):
#     endpoints = Endpoints.load(name, api_spec)
#     return endpoints


def main():

    path_jira_api_spec = "jira_api_specification.yaml"
    jira_api_spec = load_api_spec("JiraAPI", path_jira_api_spec)

    print(jira_api_spec)
    #
    # jira_endpoints = load_endpoints("JiraAPI", jira_api_spec)
    #
    # print(jira_endpoints)


if __name__ == "__main__":
    main()