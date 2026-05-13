from typing import Any
from requests.exceptions import RequestException

class API_ERROR(Exception):
    def __init__(self, message: Union[str, RequestException] = None, error: Any =requests.exceptions.RequestException) -> None:
        if not message:
            message = f"AN UNKNOWN REQUEST ERROR HAS OCCURED! {error}"
        super().__init__(message)
