import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import os

# Adiciona a raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services.service_hand_analysis_synthethic import analyze_hand

player_current_hand = "Three of a Kind"

data = analyze_hand(player_current_hand)

hand_weaker_summary_sorted = pd.DataFrame(data["hand_weaker_summary_sorted"])
hand_stronger_summary_sorted = pd.DataFrame(data["hand_stronger_summary_sorted"])
hand_same_category_sorted = pd.DataFrame(data["hand_same_category_sorted"])
hand_waker_or_equal_summary_sorted = pd.concat([hand_same_category_sorted, hand_weaker_summary_sorted], ignore_index=True)

# Rótulos e tamanhos
labels = ['Você ganha', 'Você perde', 'Da mesma categoria']
sizes = [data["hands_stronger_count"], data["hands_weaker_count"], data["hands_same_category_count"]]
colors = ['#4CAF50', '#F44336', '#9E9E9E' ]

# Criar gráfico de pizza
plt.figure(figsize=(6, 6))
plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90
)
plt.title('Esta mão é boa?')
plt.axis('equal')
plt.show()

# Fazendo gráfico de barras

# Exibindo analítico das mãos mais fracas que a do jogador
plt.figure(figsize=(10, 5))

sns.barplot(
    x=hand_waker_or_equal_summary_sorted["category"],
    y=hand_waker_or_equal_summary_sorted["percentage"],
    palette='Blues_d'
)

plt.title("Porcentagem de aparição de mãos mais fortes ou tão boas quanto a sua:")
plt.xlabel("Categoria da Mão")
plt.ylabel("Porcentagem (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Exibindo analítico das mãos mais fortes que a do jogador
plt.figure(figsize=(10, 5))
sns.barplot(
    x=hand_stronger_summary_sorted["category"],
    y=hand_stronger_summary_sorted["percentage"],
    palette='Blues_d'
)

plt.title("Porcentagem de aparição de mãos mais fracas que a sua:")
plt.xlabel("Categoria da Mão")
plt.ylabel("Porcentagem (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
