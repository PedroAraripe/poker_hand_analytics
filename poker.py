import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import constants

hand_summary = pd.read_csv("hand_summary.csv")
# Categorizando mãos por mais forte, mais fraca e da mesma categoria

player_current_hand = "Two Pair"

def load_syntetic(player_hand):
    hands_weaker = hand_summary[hand_summary["hand power"] > constants.hand_category_power[player_hand]];
    hands_same_category = hand_summary[hand_summary["hand power"] == constants.hand_category_power[player_hand]];
    hands_stronger = hand_summary[hand_summary["hand power"] < constants.hand_category_power[player_hand]]

    # Resumo de força da mão
    hands_weaker_count = hands_weaker["percentage"].sum().round(2)
    hands_stronger_count = hands_stronger["percentage"].sum().round(2)
    hands_same_category_count = hands_same_category["percentage"].sum().round(2)

    # Rótulos e tamanhos
    labels = ['Você ganha', 'Você perde', 'Da mesma categoria']
    sizes = [hands_stronger_count, hands_weaker_count, hands_same_category_count]
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
    plt.title('Distribuição das Mãos em Relação à Sua Mão')
    plt.axis('equal')
    plt.show()

    # Fazendo gráfico de barras

    # Exibindo analítico das mãos mais fracas que a do jogador
    hand_weaker_summary_sorted = hands_weaker.sort_values('hand power')

    plt.figure(figsize=(10, 5))
    sns.barplot(
        x=hand_weaker_summary_sorted.index,
        y=hand_weaker_summary_sorted['percentage'],
        palette='Blues_d'
    )

    plt.title("Distribuição das Categorias de Mãos Mais Fortes")
    plt.xlabel("Categoria da Mão")
    plt.ylabel("Porcentagem (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Exibindo analítico das mãos mais fortes que a do jogador
    hand_stronger_summary_sorted = hands_stronger.sort_values('hand power')

    plt.figure(figsize=(10, 5))
    sns.barplot(
        x=hand_stronger_summary_sorted.index,
        y=hand_stronger_summary_sorted['percentage'],
        palette='Blues_d'
    )

    plt.title("Distribuição das Categorias de Mãos Mais Fortes")
    plt.xlabel("Categoria da Mão")
    plt.ylabel("Porcentagem (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

load_syntetic(player_current_hand)