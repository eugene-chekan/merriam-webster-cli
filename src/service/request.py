""" This module holds classes and methods to handle the url response over API
"""
import os
from typing import Optional

import requests

from defines import BASE_URL


class Response:
    def __init__(self, *, api_key: Optional[str] = None):
        self.api_key = os.getenv("DICT_API_KEY") if api_key is None else api_key

    def url_construct(self, search_word):
        """ Construct an appropriate URL with the given search word
        """
        final_url = "/".join((BASE_URL, search_word))
        return final_url

    def get_response(self, dict_url: str):
        """ Get response from the given URL as a json string
        """
        response = requests.get(dict_url, params={"key": self.api_key})
        return response
