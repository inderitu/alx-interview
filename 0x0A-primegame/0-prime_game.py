#!/usr/bin/python3
"""
find winner in a prime number picking game
"""


def get_primes(n: int) -> int:
    """
    check if n is a prime mumber
    """
    if n < 2 or (n % 2 == 0 and n > 2):
        return False
    else:
        for i in range(3, int(n**(1/2))+1, 2):
            if n % i == 0:
                return "Not prime"
        return True


def round_winner(n, x):
    """
    find winner of each round
    """
    players = ['Maria', 'Ben']
    list = [i for i in range(1, n + 1)]

    for i in range(n):
        current_player = players[i % 2]
        selectedIdxs = []
        prime = -1

        for idx, num in enumerate(list):
            if prime != -1:
                if num % prime == 0:
                    selectedIdxs.append(idx)
            else:
                if get_primes(num):
                    selectedIdxs.append(idx)
                    prime = num
        if prime == -1:
            if current_player == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            for idx, val in enumerate(selectedIdxs):
                del list[val - idx]
    return None


def isWinner(x, nums):
    '''finds the winner'''
    winnerCounter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        roundWinner = round_winner(nums[i], x)
        if roundWinner is not None:
            winnerCounter[roundWinner] += 1

    if winnerCounter['Maria'] > winnerCounter['Ben']:
        return 'Maria'
    elif winnerCounter['Ben'] > winnerCounter['Maria']:
        return 'Ben'
    else:
        return None
