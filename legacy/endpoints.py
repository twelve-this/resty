from dataclasses import dataclass, field


@dataclass
class Endpoints:
    endpoints: dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_definition(cls, endpoint_definitions: list[omegaconf.ListConfig]) -> 'Endpoints':
        endpoints = cls()
        endpoints.endpoints = {endpoint.name: Endpoint(**endpoint) for endpoint in endpoint_definitions}
        return endpoints



@dataclass
class Endpoint:
    name: str
    url: str
    method: str
    params: dict[str, str] = field(default_factory=dict)
    headers: dict[str, str] = field(default_factory=dict)
    body: dict[str, str] = field(default_factory=dict)