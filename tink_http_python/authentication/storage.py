from abc import ABC, abstractmethod


class Storage:
    @abstractmethod
    def retrieve_authorization_code(self) -> str:
        pass

    @abstractmethod
    def store_new_authorization_code(self, new_authorization_code: str) -> str:
        pass
