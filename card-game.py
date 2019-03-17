
n = int(input())
cards2 = [int(_) for _ in input().split()]
cards = list(cards2)
play_sequence = []


def max_reward(play_sequence, card_index):
    # print(play_sequence)
    # print(card_index)
    # print(cards)
    if card_index == n - 1:
        if cards[card_index] * cards[card_index - 1] > 0:
            play_sequence.append(card_index)
            cards[card_index] = 1
    else:
        if card_index == 0:
            left_value = 1
        else:
            left_value = cards[card_index-1]
        if cards[card_index] * left_value < cards[card_index] * cards[card_index + 1] * left_value:
            if cards[card_index] * cards[card_index + 1] * left_value < 0:
                return max_reward(play_sequence, card_index+1)
            play_sequence.append(card_index)
            cards[card_index] = 1
            play_sequence = max_reward(play_sequence, card_index+1)
        elif cards[card_index] * left_value <= 0 and cards[card_index] * cards[card_index + 1] * left_value <= 0:
            play_sequence = max_reward(play_sequence, card_index+1)
        elif cards[card_index] * left_value == cards[card_index] * cards[card_index + 1] * left_value:
            if cards[card_index] < cards[card_index + 1] and cards[card_index] * cards[card_index + 1] * left_value > 0:
                # print("cards", cards)
                # print("index", card_index)
                play_sequence.append(card_index)
                cards[card_index] = 1
            play_sequence = max_reward(play_sequence, card_index+1)

        else:
            play_sequence = max_reward(play_sequence, card_index+1)
            play_sequence.append(card_index)
            return play_sequence
    return play_sequence


play_sequence = max_reward(play_sequence, 0)
reward = 0
for item in play_sequence:
    
    if item == 0:
        left = 1
    else:
        left = cards2[item-1]
    if item == n-1:
        right = 1
    else:
        right = cards2[item+1]
    # print(cards2[item], cards2[item] * left * right)
    reward += cards2[item] * left * right
    cards2[item] = 1
# print(play_sequence)
print(reward)

