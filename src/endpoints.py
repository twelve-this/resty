from dataclasses import dataclass, field
from typing import Any

from src.endpoint import Endpoint
from src.endpoint_specs import APISpec


@dataclass
class Endpoints:

    name: str
    endpoint_specs: APISpec = field(repr=False)
    global_headers: dict[str, str] = field(init=False, default_factory=dict)
    endpoints: dict[str, Endpoint] = field(init=False, default_factory=dict)

    @classmethod
    def load(cls, name: str, endpoint_specs: APISpec) -> "Endpoints":
        endpoints = cls(name, endpoint_specs)
        return endpoints

    def __post_init__(self) -> None:
        self._load_global_headers()
        self._load_endpoints()

    def _load_global_headers(self) -> None:
        self.global_headers = self.endpoint_specs.global_headers

    def _load_endpoints(self) -> None:
        endpoints = {}
        for key, value in self.endpoint_specs.endpoints.items():
            params = {"name": key} | value
            endpoint = Endpoint(**params)
            endpoints[key] = endpoint
        self.endpoints = endpoints

