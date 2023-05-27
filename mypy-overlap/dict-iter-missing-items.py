# Both correctly positive.
data = {"Paris": 2_165_423, "New York City": 8_804_190, "Tokyo": 13_988_129}
for city, population in data:  # [dict-iter-missing-items]
    print(f"{city} has population {population}.")


# Both correctly negative.
other_data = {(1, 2): 1, (2, 3): 2}
for a, b in other_data:
    print(a, b)

