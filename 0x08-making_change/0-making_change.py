"""
Module determining  the fewest number of coins neede to meetgiven amount total
"""


def makeChange(coins, total):
    """
    Chooses minimum number of coins to meet a given total
    Args:
        coins (list of ints): list of coints of different values.
        total (int): total value that must be met.
    Return:
        Number of coins or -1 if the meeting total is not possible
    """
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        x = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    count_coin = 0
    for y in coins:
        if total % y == 0:
            count_coin += int(total / y)
            return count_coin
        if total - y >= 0:
            if int(total / y) > 1:
                count_coin += int(total / y)
                total = total % y
            else:
                count_coin += 1
                total -= y
                if total == 0:
                    break
    if total > 0:
        return -1
    return count_coin
