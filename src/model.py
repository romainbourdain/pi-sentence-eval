class Model:
    def __init__(self, model_name: str, params: str):
        self.model_name = model_name
        self.params = params

    def __str__(self) -> str:
        return f"{self.model_name}:{self.params}"
