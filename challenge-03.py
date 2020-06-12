'''
Python v3.8 or later
Windows 10
For fun.
DESCRIPTION: Page Source
OWNER: Roan Fourie
REVISION: 0
REVISION DATE: 2020-06-12 (Week 24)
REVISION AUTHOR: Roan Fourie
REVISION DESCRIPTION:
    One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

    View source in page source.
    
    data was pasted into challenge-03.txt

NOTES:
    http://www.pythonchallenge.com/pc/def/equality.html  
    Thus something like: ABCxDEF
'''
import re

result = []
result2 = ''
with open('challenge-03.txt', 'r') as fi:
    for line in fi:
        # result.append(re.findall(r"([a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z])\w", line))
        # result.append(re.findall(r"([A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z])\w", line))
        result.append(re.findall(r"[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", line))


res = [x for x in result if x]
print(res)
a = []
res1 = [x[0] for x in res]
print(res1)
result2 = "".join([x for x in res1])
print(result2)

# http://www.pythonchallenge.com/pc/def/linkedlist.php

# First result I got was: ['qIQNlQSLi', 'eOEKiVEYj', 'aZADnMCZq', 'bZUTkLYNg', 'uCNDeHSBj', 'kOIXdKBFh', 'dXJVlGZVm', 'gZAGiLQZx', 'vCJAsACFl', 'qKWGtIDCj']
# The question was not very clear to me.
# After some googling, I found that if you look inside between the body guards, you get these characters:
# ['l', 'i', 'n', 'k', 'e', 'd', 'l', 'i', 's', 't']