from enum import Enum


class Pronoun(Enum):
    IL: tuple[str, str] = ("il", "blue")
    ELLE: tuple[str, str] = ("elle", "orange")
    OTHER: tuple[str, str] = ("autre", "green")

    def __init__(self, label: str, color: str) -> None:
        self._label: str = label
        self._color: str = color

    @property
    def label(self) -> str:
        return self._label

    @property
    def color(self) -> str:
        return self._color
