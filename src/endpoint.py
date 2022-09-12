from typing import Optional, Dict, List

from pydantic import BaseModel, Field, validator


class Endpoint(BaseModel):

    name: str
    url: str
    verb: str
    global_headers: Dict[str, str]
    additional_headers: Dict[str, str]
    remove_global_headers: List[str]
    path_parameters: List[str]
    query_parameters: Dict[str, str]

    _actual_path_parameters: Dict[str, str] = Field(default_factory=dict)

    @property
    def headers(self) -> Dict[str, str]:
        headers = {**self.global_headers, **self.additional_headers}
        return self._remove_global_headers(headers)

    @property
    def ready_url(self) -> str:
        pass

    @property
    def has_path_parameters_in_url(self) -> bool:
        return bool(self.path_parameters)

    @property
    def path_parameters_provided(self) -> bool:

        if not self.has_path_parameters_in_url:
            return False

        for path_parameter in self.path_parameters:
            if path_parameter not in self._actual_path_parameters:
                return False
        return True

    def provide_path_parameters(self, path_parameters: Dict[str, str]) -> None:
        self._actual_path_parameters.update(path_parameters)

    def _remove_global_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        if not self.global_headers:
            return headers
        return {key: value for key, value in headers.items() if key not in self.remove_global_headers}




