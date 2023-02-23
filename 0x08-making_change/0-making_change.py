#!/usr/bin/python3
"""Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """return minimum number coins"""
    if total <= 0:
        return 0

    fewest_number = 0
    current_total = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        alredy_used = (total - current_total) // coin
        current_total += alredy_used * coin
        fewest_number += alredy_used
        pass
        if current_total == total:
            return fewest_number
    return - 1
