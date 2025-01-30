import re
from typing import Optional

from src.pronoun import Pronoun
from src.types import Hyperparameters


class LLMResponse:
    def __init__(
        self,
        prompt: str,
        response: str,
        model: str,
        hyperparameters: Optional[Hyperparameters] = None,
    ) -> None:
        self.prompt: str = prompt
        self.response: str = response
        self.model: str = model
        self.hyperparameters: Optional[Hyperparameters] = hyperparameters

    def _format_response(self, response: str) -> str:
        formated_response: str = re.sub(r"[^a-zA-Z0-9 ]", "", response)
        return formated_response.lower()

    def get_pronoun(self) -> Pronoun:
        il_entry: str = self._format_response(self.prompt.replace("___", "il"))
        elle_entry: str = self._format_response(self.prompt.replace("___", "elle"))

        il_pos: int = self._format_response(self.response).find(il_entry)
        elle_pos: int = self._format_response(self.response).find(elle_entry)

        match il_pos, elle_pos:
            case -1, -1:
                return Pronoun.OTHER
            case _, -1:
                return Pronoun.IL
            case -1, _:
                return Pronoun.ELLE
            case _, _:
                return Pronoun.OTHER

        return Pronoun.OTHER

    def __str__(self) -> str:
        return self.response
