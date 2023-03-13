#!/usr/bin/python3
def multiple_returns(sentence):
   if sentence or len(sentence) > 0:
      return (len(sentence), sentence[0])
