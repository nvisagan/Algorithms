#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Create Options
  hand = [["rock"], ["paper"], ["scissors"]]
  #Base Case
  if n == 0:
    return [[]]
  if n == 1:
    return hand

  combos = []
  #recursive call
  rounds = rock_paper_scissors(n-1)
  for round in rounds:
    for play in hand:
      next_play = round + play
      combos.append(next_play)
  
  return combos

print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')