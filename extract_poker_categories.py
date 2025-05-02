import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import constants;

df = pd.read_csv("poker_hands_full.csv")

# Contagem e proporção
hand_category_power_distribution = df["category"].value_counts().sort_values(ascending=False)
hand_percentages = (hand_category_power_distribution / len(df) * 100).round(5)


# Juntar contagem e porcentagem em um DataFrame
hand_summary = pd.DataFrame({
    "hand": hand_category_power_distribution,
    "percentage": hand_percentages,
})

hand_summary["hand power"] = hand_summary.index.map(constants.hand_category_power)
hand_summary.to_csv("hand_summary.csv", index_label="category")