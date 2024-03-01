import requests
from requests import Response


class ApiRequests:
"""
wrapper class for api requests that includes built in allure logging.
"""


@staticmethod
def get(path: str, params=None) -> Response:
    response = requests.get(path, params=params)
    return response


@staticmethod
def post(path: str, data=None, params=None) -> Response:
    response = requests.post(path, params=params, json=data)
    return response


@staticmethod
def delete(path: str) -> Response:
    response = requests.delete(path)
    return response


@staticmethod
def put(path: str, data=None, params=None) -> Response:
    response = requests.put(path, params=params, json=data)
    return response