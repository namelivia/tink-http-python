from abc import ABC, abstractmethod


class Storage:
    @abstractmethod
    def store_new_refresh_token_refresh_token(self, new_refresh_token) -> str:
        pass

    @abstractmethod
    def retrieve_refresh_token(self) -> str:
        pass

    @abstractmethod
    def retrieve_authorization_code(self) -> str:
        pass
