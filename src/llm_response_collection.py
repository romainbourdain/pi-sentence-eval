from typing import List

import matplotlib.pyplot as plt
import pandas as pd

from src.llm_response import LLMResponse


class LLMResponseCollection:
    def __init__(self, responses: List[LLMResponse]) -> None:
        self.df = pd.DataFrame(
            [
                {
                    "model": response.model,
                    "temperature": response.hyperparameters["temperature"]
                    if "temperature" in response.hyperparameters
                    else None,
                    "top_p": response.hyperparameters["top_p"]
                    if "top_p" in response.hyperparameters
                    else None,
                    "top_k": response.hyperparameters["top_k"]
                    if "top_k" in response.hyperparameters
                    else None,
                    "prompt": response.prompt,
                    "response": response.response,
                    "category": response.get_pronoun().label,
                }
                for response in responses
            ]
        )

    def plot_evolution(self, x_column: str) -> None:
        """
        Affiche un graphique en barres empilées des catégories de réponses en fonction d'un paramètre choisi.

        Paramètres :
        - df : DataFrame contenant les réponses
        - x_column : Colonne à utiliser comme axe X (par défaut : 'model')
        """
        grouped = self.df.groupby([x_column, "category"]).size().unstack(fill_value=0)

        grouped.plot(kind="bar", stacked=True, figsize=(10, 6))

        plt.xlabel(x_column)
        plt.ylabel("Nombre d'occurrences")
        plt.title(f"Répartition des catégories en fonction de {x_column}")
        plt.xticks(rotation=45)
        plt.legend(title="Catégorie de réponse")

        plt.show()

    def plot_pie_chart(self) -> None:
        """
        Affiche un diagramme en camembert de la répartition des catégories de réponses.

        Paramètres :
        - df : DataFrame contenant les réponses avec une colonne 'category'
        """
        category_counts = self.df["category"].value_counts()

        plt.figure(figsize=(8, 8))
        plt.pie(
            category_counts,
            labels=category_counts.index,
            autopct="%1.1f%%",
            startangle=90,
            wedgeprops={"edgecolor": "black"},
        )

        plt.title("Répartition des catégories de réponses")
        plt.show()
