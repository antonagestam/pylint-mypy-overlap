def pick_fruits(fruits) -> None:
    for fruit in fruits:
        print(fruit)


pick_fruits(["apple"])[0] = "orange"  # [unsupported-assignment-operation]

