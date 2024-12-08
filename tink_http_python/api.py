import requests
import logging
from abc import ABC, abstractmethod


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class AbstractAPI(ABC):
    @abstractmethod
    def _get_url_base(self) -> str:
        pass

    def _build_url(self, uri) -> str:
        return self._get_url_base() + uri

    def post(self, uri: str, headers: dict, data: dict) -> dict:
        response = requests.post(self._build_url(uri), data=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def get(self, uri: str, headers: dict) -> dict:
        response = requests.get(self._build_url(uri), headers=headers)
        response.raise_for_status()
        logger.debug(f"Response body: {response.text}")
        data = response.json()
        return data


class ApiV1(AbstractAPI):
    def _get_url_base(self) -> str:
        return "https://api.tink.com/api/v1/"


class ApiV2(AbstractAPI):
    def _get_url_base(self) -> str:
        return "https://api.tink.com/data/v2/"
