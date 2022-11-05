import requests
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    @abstractmethod
    def _get_url_base(self) -> str:
        pass

    def _build_url(self, uri) -> str:
        return self._get_url_base() + uri

    def post(self, uri: str, headers: dict, data: dict) -> dict:
        response = requests.post(self._build_url(uri), data=data, headers=headers)
        if response.status_code == 200:
            return response.json()
        print(response.__dict__)
        exit()

    def get(self, uri: str, headers: dict) -> dict:
        response = requests.get(self._build_url(uri), headers=headers)
        if response.status_code == 200:
            return response.json()
        print(response.__dict__)
        exit()


class ApiV1(AbstractAPI):
    def _get_url_base(self) -> str:
        return "https://api.tink.com/api/v1/"


class ApiV2(AbstractAPI):
    def _get_url_base(self) -> str:
        return "https://api.tink.com/data/v2/"
