import json
from typing import Dict
import requests
from requests import Response
from pydantic import BaseModel


class CallOptionPrice(BaseModel):
    stock: str # the field name is case sensitive
    price: float


# def get_call_option_price() -> Dict[str, float]:
def get_call_option_price() -> CallOptionPrice:

    """
    Makes a GET request to our call option price predictor service
    """
    url: str = "http://localhost:6000/call_option_price"

    data: Dict[str, str] = {
        "stock": "AAPL"
    }

    # GET, POST, PUT, DELETE, UPDATE
    # TLDR: people normally only use GET and POST
    # On the server, we are getting the "data" field  from the request; this means
    # we need to pass in the input data (data), under the "data" field, instead of under params
    response: Response = requests.get(
        url=url,
        data=json.dumps(data)
    )
    # to check for type hints: print the type(object)
    # print(f"response: {type(response)}")
    response_json: Dict[str, float] = response.json()

    # converting a dictionary into a data class; pydantic.BaseModel
    call_option_price: CallOptionPrice = CallOptionPrice.parse_obj(response_json)
    return call_option_price


if __name__ == "__main__":
    call_option_price: CallOptionPrice = get_call_option_price()

    # Test: pydantic.BaseModel provides type safety; it doesn't allow us to pass the wrong type to the field
    # call_option_price: CallOptionPrice = CallOptionPrice(stock="AAPL", price="100-1")

    print(call_option_price)