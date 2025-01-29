
def process_test_cases(num_test_cases, test_cases_data):
    results = []
 
    for case in test_cases_data:
        num_decks, num_rounds, deck_list = case
        
        for deck in deck_list:
            deck.sort()
        
        smallest_cards = [(deck[0], index) for index, deck in enumerate(deck_list)]
        smallest_cards.sort() 
        
        deck_order = [card_info[1] + 1 for card_info in smallest_cards]  
        is_valid = True
        top_card = -1
        
        for _ in range(num_rounds):
            current_round_cards = []
            for cow in deck_order:
                cow_index = cow - 1 
                if deck_list[cow_index] and deck_list[cow_index][0] > top_card:
                    top_card = deck_list[cow_index].pop(0)
                else:
                    is_valid = False
                    break
            if not is_valid:
                break
        
        if is_valid:
            results.append(" ".join(map(str, deck_order)))
        else:
            results.append("-1")
 
    return results


num_test_cases = int(input())
test_cases_data = []
for _ in range(num_test_cases):
    num_decks, num_rounds = map(int, input().split())
    deck_list = [list(map(int, input().split())) for _ in range(num_decks)]
    test_cases_data.append((num_decks, num_rounds, deck_list))
 
outcomes = process_test_cases(num_test_cases, test_cases_data)
print("\n".join(outcomes))