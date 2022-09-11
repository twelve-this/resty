from typing import Any, Optional

from pydantic import BaseModel, root_validator

from src.endpoint import Endpoint


class APISpec(BaseModel):

    name: str
    global_headers: dict[str, str]
    endpoints_raw: dict[str, dict]
    endpoints: dict[str, Endpoint]

    @root_validator(pre=True)
    def create_endpoints(cls, values):
        endpoints = {}
        for key, value in values["endpoints_raw"].items():
            params = {"name": key, "global_headers": values["global_headers"]} | value
            endpoint = Endpoint(**params)
            endpoints[key] = endpoint
        values["endpoints"] = endpoints
        return values

    def get_endpoint(self, name) -> Endpoint:
        return self.endpoints[name]
