from typing import Any

from pydantic import BaseModel


class APISpec(BaseModel):

    name: str
    global_headers: dict[str, str]
    endpoints: dict[str, Any]


