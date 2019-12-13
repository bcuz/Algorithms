#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n <= 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4

  return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies( n - 1)

print(eating_cookies(0))

# 4 cookie brainstorm
# He can eat 1 cookie at a time 4 times
# He can eat 1 cookie, 1 cookie, then 2 cookies
# He can eat 1 cookie, 2 cookies, then 1 cookies
# He can eat 2 cookie, 1 cookies, then 1 cookies
# He can eat 2 cookies, then 2 cookies
# He can eat 1 cookies, then 3 cookies
# He can eat 3 cookies, then 1 cookies

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')