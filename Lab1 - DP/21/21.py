import time, tracemalloc

def can_defend(trump_suit, player_cards, attack_cards):
    ranks = {'6': 0, '7': 1, '8': 2, '9': 3, 'T': 4, 'J': 5, 'Q': 6, 'K': 7, 'A': 8}

    player_cards_by_suit = {suit: [] for suit in 'SCDH'}
    for card in player_cards:
        player_cards_by_suit[card[1]].append(card)

    for suit in player_cards_by_suit:
        player_cards_by_suit[suit].sort(key=lambda x: ranks[x[0]])

    for attack_card in attack_cards:
        attack_rank, attack_suit = attack_card[0], attack_card[1]

        possible_defense = [c for c in player_cards_by_suit[attack_suit] if ranks[c[0]] > ranks[attack_rank]]

        if attack_suit == trump_suit:
            possible_defense = [c for c in possible_defense if c[1] == trump_suit]

        if not possible_defense and attack_suit != trump_suit:
            possible_defense = player_cards_by_suit[trump_suit]

        if not possible_defense:
            return "NO"

        used_card = possible_defense[0]
        player_cards_by_suit[used_card[1]].remove(used_card)

    return "YES"

with open("input.txt", "r") as file:
    first_line = file.readline().strip().split()
    N, M, trump_suit = int(first_line[0]), int(first_line[1]), first_line[2]
    player_cards = file.readline().strip().split()
    attack_cards = file.readline().strip().split()

start_time = time.perf_counter()
tracemalloc.start()

result = can_defend(trump_suit, player_cards, attack_cards)

end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {(end_time - start_time):.6f} секунд")
print(f"Использовано памяти: {(peak_memory / (1024 * 1024)):.6f} Мб")



with open("output.txt", "w") as file:
    file.write(result + "\n")
