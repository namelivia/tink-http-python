from abc import ABC, abstractmethod


class Storage:
    @abstractmethod
    def retrieve_authorization_code(self) -> str:
        pass

    @abstractmethod
    def store_new_authorization_code(self, new_authorization_code: str) -> str:
        pass

    @abstractmethod
    def retrieve_access_token(self) -> str:
        pass

    @abstractmethod
    def store_new_access_token(self, new_access_token: str) -> str:
        pass
