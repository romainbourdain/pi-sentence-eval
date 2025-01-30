from typing import Optional, TypedDict

Hyperparameters = TypedDict(
    "Hyperparameters",
    {
        "temperature": Optional[float],
        "top_p": Optional[float],
        "top_k": Optional[float],
        "seed": Optional[int],
    },
)
