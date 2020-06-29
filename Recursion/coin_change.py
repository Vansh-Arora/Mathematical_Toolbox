# Produce change for all possible amounts starting with 8, 
# Using only coins of denomination 3 & 5.

def change(amount):
    assert(amount >= 8)
    if amount == 8:
        return [3,5]
    if amount == 9:
        return [3,3,3]
    if amount == 10:
        return [5,5]
    # If amount is greater than 10
    coins = change(amount - 3) # Decrease the amount to reach the base case
    coins.append(3) # Since we removed 3
    return coins

if __name__ == "__main__":
    print(change(20))
    print(change(1100))