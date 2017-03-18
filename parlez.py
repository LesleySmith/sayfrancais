#!/bin/python
# Chooses an input list to import and prints a random line
# basically it's fortune with my own fortunes

# argument parsing - choose which vocab list(s) to load
import argparse
parser = argparse.ArgumentParser(description="parse which vocab lists to load")

# different files which exist
parser.add_argument('-c','--cats', dest='docats', action='store_true', default=False)
parser.add_argument('-v','--verbs', dest='doverbs', action='store_true', default=False)
args = parser.parse_args()

totallist = [""]

if(args.docats):
 from cats import cats
 totallist+=cats

if(args.doverbs):
 from verbs import verbs
 totallist+=verbs
 
import random
print(random.choice(totallist))
