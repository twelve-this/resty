from dataclasses import field, dataclass


@dataclass
class Endpoints:
    endpoints: list[dict] = field(default_factory=list)


@dataclass
class Actions:
    migrate: str
    get_test_execution_data: str


@dataclass
class Paths:
    output: str
    input: str


@dataclass
class Config:
    endpoints: Endpoints
    actions: Actions
    paths: Paths
