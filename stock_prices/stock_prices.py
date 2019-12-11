#!/usr/bin/python

import argparse


def find_max_profit(prices):
    max_profit = [0]

    for i in range(0, len(prices) - 1):
        cur_index = i

        for x in range(cur_index + 1, len(prices) - 1):

            if prices[x] - prices[cur_index] > max_profit[0]:
                max_profit[0] = prices[x] - prices[cur_index]

            elif prices[x] - prices[cur_index] < 0 and max_profit[0] == 0:
                max_profit[0] = prices[x] - prices[cur_index]

            elif prices[x] - prices[cur_index] > max_profit[0]:
                max_profit[0] = prices[x] - prices[cur_index]

            # elif prices[x] - prices[cur_index] < 0 and max_profit[0] == 0:
            #     max_profit[0] = prices[x] - prices[cur_index]

    return max_profit[0]


if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
