from pydantic.dataclasses import dataclass


@dataclass
class Value:
    unscaled_value: str
    scale: str


@dataclass
class Amount:
    value: Value
    currency_code: str
