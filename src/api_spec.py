from typing import Dict

from pydantic import BaseModel, root_validator

from src.endpoint import Endpoint


class APISpec(BaseModel):

    name: str
    global_headers: Dict[str, str]
    endpoints_raw: Dict[str, dict]
    endpoints: Dict[str, Endpoint]

    @root_validator(pre=True)
    def create_endpoints(cls, values):
        endpoints = {}
        for key, value in values["endpoints_raw"].items():
            params = {**{"name": key, "global_headers": values["global_headers"]}, **value}
            endpoint = Endpoint(**params)
            endpoints[key] = endpoint
        values["endpoints"] = endpoints
        return values

    def get_endpoint(self, name) -> Endpoint:
        return self.endpoints[name]
