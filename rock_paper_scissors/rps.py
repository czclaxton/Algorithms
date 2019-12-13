#!/usr/bin/python

import sys

# Recursive Solution


def rock_paper_scissors(n):
    possible_plays = []

    def rps(n, prefix=[]):
        if n == 0:
            possible_plays.append(prefix)
        else:
            rps(n-1, prefix + ['rock'])
            rps(n-1, prefix + ['paper'])
            rps(n-1, prefix + ['scissors'])
    rps(n)
    return possible_plays

# Iterative Solution

# def rock_paper_scissors(n):
#     output = []
#     possible_plays = ['scissors', 'paper', 'rock']
#     stack = []
#     stack.append([])
#     while len(stack) > 0:
#         hand = stack.pop()
#         if n == 0 or len(hand) == n:
#             output.append(hand)
#         else:
#             for play in possible_plays:
#                 stack.append(hand + [play])
#     return output


# plays = ['rock', 'paper', 'scissors']

# def rock_paper_scissors(n):
#     possible_plays = [[]]
#     if n <= 0:
#         return possible_plays
#     def rps(n):
#         nonlocal possible_plays
#         if n <= 1:
#             return [[play] for play in plays]
#         else:
#             possible_plays = rps(n-1)
#             result = []
#             for x in possible_plays:
#                 new_plays = []
#                 for y in plays:
#                     new_plays.append(x + [y])
#                 result = result + new_plays
#             return result
#     return rps(n)
if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
