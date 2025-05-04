
import pandas as pd
from constants.cards_combinations_powers import hand_category_power

def analyze_hand(player_current_hand: str):
  hand_summary = pd.read_csv("data/hand_summary.csv")

  player_hand_category_level = hand_category_power[player_current_hand]

  hands_weaker = hand_summary[hand_summary["hand power"] > player_hand_category_level];
  hands_stronger = hand_summary[hand_summary["hand power"] < player_hand_category_level]
  hands_same_category = hand_summary[hand_summary["hand power"] == player_hand_category_level];

  # Resumo de força da mão
  hands_weaker_count = hands_weaker["percentage"].sum().round(5)
  hands_stronger_count = hands_stronger["percentage"].sum().round(5)
  print(hands_stronger["hand"].sum())
  hands_same_category_count = hands_same_category["percentage"].sum().round(5)
  hands_weaker_total_count = hands_weaker["hand"].sum().round(5)
  hands_stronger_total_count = hands_stronger["hand"].sum()
  hands_same_category_total_count = hands_same_category["hand"].sum().round(5)

  hand_weaker_summary_sorted = hands_weaker.sort_values('hand power')
  hand_stronger_summary_sorted = hands_stronger.sort_values('hand power')
  hand_same_category_sorted = hands_same_category.sort_values('hand power')

  return {
      "player_current_hand": player_current_hand,
      "hands_weaker_count": hands_weaker_count,
      "hands_stronger_count": hands_stronger_count,
      "hands_same_category_total_count": int(hands_same_category_total_count),
      "hands_weaker_total_count": int(hands_weaker_total_count),
      "hands_stronger_total_count": int(hands_stronger_total_count),
      "hands_same_category_count": hands_same_category_count,
      "hand_weaker_summary_sorted": hand_weaker_summary_sorted.to_dict(orient="records"),
      "hand_stronger_summary_sorted": hand_stronger_summary_sorted.to_dict(orient="records"),
      "hand_same_category_sorted": hand_same_category_sorted.to_dict(orient="records")
  }