# Give change for amount in range of 24-1000
# Coin denominations: 5 and 7
def change(amount):
    assert(amount >= 24)
    if amount == 24:
        return [5,5,7,7]
    if amount == 25:
        return [5,5,5,5,5]
    if amount == 26:
        return [5,7,7,7]
    if amount == 27:
        return [5,5,5,5,7]
    if amount == 28:
        return [7,7,7,7]
    # if amount > 28
    coins = change(amount - 5)
    coins.append(5)
    return(coins)

if __name__ == "__main__":
    print(change(int(input())))
