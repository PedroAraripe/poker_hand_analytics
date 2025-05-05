import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "constants")))

# Agora, importa a função corretamente
from cards_combinations_powers import hand_category_power

def transform():
    df = pd.read_csv("data/poker_hands_full.csv")

    # Contagem e proporção
    hand_category_power_distribution = df["category"].value_counts().sort_values(ascending=False)
    hand_percentages = (hand_category_power_distribution / len(df) * 100).round(5)

    # Juntar contagem e porcentagem em um DataFrame
    hand_summary = pd.DataFrame({
        "hand": hand_category_power_distribution,
        "percentage": hand_percentages,
    })

    hand_summary["hand power"] = hand_summary.index.map(hand_category_power)
    return hand_summary