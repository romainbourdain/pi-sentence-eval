from typing import Optional

import ollama

from src.llm_response import LLMResponse
from src.types import Hyperparameters


class LLMGenerator:
    def __init__(self, system_prompt: str, model: str) -> None:
        self.system_prompt = system_prompt
        self.model = model

        ollama.pull(self.model)

    def generate(
        self,
        prompt: str,
        hyperparameters: Optional[Hyperparameters] = None,
    ) -> LLMResponse:
        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt},
            ],
            options=hyperparameters,
        )

        return LLMResponse(
            prompt=prompt, response=response["message"]["content"], model=self.model
        )
