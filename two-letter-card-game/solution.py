def solve(cards: list[str], x: str) -> int:
    from collections import defaultdict

    # Filter cards that contain the letter x
    filtered_cards = [card for card in cards if x in card]

    # Count occurrences of each character position
    count_first_pos = defaultdict(int)
    count_second_pos = defaultdict(int)

    for card in filtered_cards:
        if card[0] == x:
            count_first_pos[card[1]] += 1
        else:
            count_second_pos[card[0]] += 1

    # Calculate the maximum number of compatible pairs
    max_points = 0
    for char, count in count_first_pos.items():
        if char in count_second_pos:
            max_points += min(count, count_second_pos[char])

    return max_points // 2