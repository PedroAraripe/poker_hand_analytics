import itertools

def extract():
    # Definindo os valores e naipes
    values = '23456789TJQKA'
    suits = 'CDHS'  # Clubs, Diamonds, Hearts, Spades
    deck = [v + s for v in values for s in suits]

    # Ordem de valor para facilitar comparações
    value_order = {v: i for i, v in enumerate(values, start=2)}

    # Função para avaliar uma mão
    def evaluate_hand(hand):
        suits_in_hand = [card[1] for card in hand]
        values_in_hand = [card[0] for card in hand]

        counts = {v: values_in_hand.count(v) for v in set(values_in_hand)}
        counts_sorted = sorted(counts.values(), reverse=True)
        unique_vals = sorted([value_order[v] for v in set(values_in_hand)], reverse=True)

        is_flush = len(set(suits_in_hand)) == 1
        is_straight = (
            len(set(unique_vals)) == 5 and unique_vals[0] - unique_vals[-1] == 4
        )
        # Caso especial para A-2-3-4-5
        if set(values_in_hand) == set("A2345"):
            is_straight = True

        if is_flush and set(values_in_hand) == set("TJQKA"):
            return "Royal Flush"
        elif is_flush and is_straight:
            return "Straight Flush"
        elif 4 in counts_sorted:
            return "Four of a Kind"
        elif 3 in counts_sorted and 2 in counts_sorted:
            return "Full House"
        elif is_flush:
            return "Flush"
        elif is_straight:
            return "Straight"
        elif 3 in counts_sorted:
            return "Three of a Kind"
        elif counts_sorted.count(2) == 2:
            return "Two Pair"
        elif 2 in counts_sorted:
            return "One Pair"
        else:
            return "High Card"
        
    hands = [
        {
            "category": evaluate_hand(hand),
            "hand_str": " ".join(hand)
        } for hand in itertools.combinations(deck, 5)
    ]

    return hands