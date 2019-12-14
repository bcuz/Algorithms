#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # technically o(n)

  # find lowest value that isnt the last index
  pricesWithoutLast = prices[:-1]

  lowest = min(pricesWithoutLast)

  indexOfLowest = prices.index(lowest)

  # get prices to the right of our lowest
  searchSpace = prices[indexOfLowest+1:]

  # find the highest value in searchSpace
  highest = max(searchSpace)

  return highest - lowest

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))