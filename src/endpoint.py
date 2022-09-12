from typing import Optional, Dict, List

from pydantic import BaseModel


class Endpoint(BaseModel):

    name: str
    url: str
    verb: str
    global_headers: Dict[str, str]
    additional_headers: Dict[str, str]
    remove_global_headers: List[str]
    path_parameters: List[str]
    query_parameters: Dict[str, str]

    _actual_path_parameters: Optional[Dict[str, str]] = None

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

    def _remove_global_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        if not self.global_headers:
            return headers
        return {key: value for key, value in headers.items() if key not in self.remove_global_headers}




