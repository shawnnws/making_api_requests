from typing import Dict
import requests
from requests import Response


def get_call_option_price() -> Dict[str, float]:
    url: str = "http://localhost:6000/call_option_price"
    response: Response = requests.get(
        url=url
    )
    # to check for type hints: print the type(object)
    # print(f"response: {type(response)}")
    response_json: Dict[str, float] = response.json()
    return response_json


if __name__ == "__main__":
    call_option_price: Dict[str, float] = get_call_option_price()
    print(call_option_price)