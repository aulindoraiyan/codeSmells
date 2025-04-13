ITEM_PRICES = {
    "apple": 1.00,
    "banana": 0.50,
    "cherry": 0.75,
    "mango": 1.00,
    "pineapple": 1.50,
    "dragonfruit": 2.00,
    "durian": 2.75
}

DISCOUNT_THRESHOLD = 10.0
DISCOUNT_RATE = 0.9

def calculate_total_price(items):
    total = 0.0
    for item in items:
        price = ITEM_PRICES.get(item)
        if price is not None:
            total += price
        else:
            print(f"Unknown item: {item}")
    
    if total >= DISCOUNT_THRESHOLD:
        total *= DISCOUNT_RATE
    
    return total


if __name__ == "__main__":
    print("run `pytest tests/smells1_test.py` instead.")
