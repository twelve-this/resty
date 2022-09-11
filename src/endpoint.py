from collections import ChainMap
from typing import Mapping

from pydantic import BaseModel, root_validator


class Endpoint(BaseModel):

    name: str
    url: str
    verb: str
    global_headers: dict[str, str]
    additional_headers: dict[str, str]
    remove_global_headers: list[str]
    path_parameters: dict[str, str]
    query_parameters: dict[str, str]

    @property
    def headers(self) -> dict[str, str]:
        headers = self.global_headers | self.additional_headers
        return self._remove_global_headers(headers)

    def _remove_global_headers(self, headers: dict[str, str]) -> dict[str, str]:
        if not self.global_headers:
            return headers
        return {key: value for key, value in headers.items() if key not in self.remove_global_headers}




