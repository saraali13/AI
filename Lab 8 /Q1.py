total_cards = 52

# Red cards (hearts + diamonds)
red_cards = 26
hearts = 13
diamonds = 13

# Face cards (Jack, Queen, King): 4 suits * 3 face cards
face_cards = 12
face_diamonds = 3
# Face cards that are either spades or queens
# Spade face cards = 3, Queens (one per suit) = 4 → but Queen of Spades counted once
face_spades_or_queens = 3 + 4 - 1  # Subtract 1 to avoid double counting Queen of Spades

# Probabilities
p_red = red_cards / total_cards
p_heart_given_red = hearts / red_cards
p_diamond_given_face = face_diamonds / face_cards
p_spade_or_queen_given_face = face_spades_or_queens / face_cards

print("Probability of drawing a red card:", p_red)
print("Probability of heart given red:", p_heart_given_red)
print("Probability of diamond given face card:", p_diamond_given_face)
print("Probability of spade or queen given face card:", p_spade_or_queen_given_face)

