from pydantic import BaseModel


class Endpoint(BaseModel):

    name: str
    url: str
    verb: str
    additional_headers: dict[str, str] | None
    remove_global_headers: list[str] | None
    path_parameters: dict[str, str] | None
    query_parameters: dict[str, str] | None

