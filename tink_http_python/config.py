from pydantic.dataclasses import dataclass


@dataclass
class Config:
    client_id: str
    client_secret: str
    redirect_uri: str
