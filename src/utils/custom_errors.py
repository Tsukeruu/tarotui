from typing import Any
from requests.exceptions import RequestException

class API_ERROR(Exception):
    def __init__(self, message: Union[str, RequestException] = None, error: RequestException = None) -> None:
        if not message:
            message: str = f"AN UNKNOWN REQUEST ERROR HAS OCCURED! {error}"
        super().__init__(message)

class UNDETECTABLE_OS(Exception):
    def __init__(self, command: str, message: str = None, error: Optional[str] = None) -> None:
        if not message:
            message: str = f"OS TO RUN COMMAND: `{command}` IS UNDETECTABLE"
        super().__init__(message)
