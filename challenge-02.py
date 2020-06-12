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
    recognize the characters. maybe they are in the book,
    but MAYBE they are in the page source.

    <!--
    find rare characters in the mess below:
    -->

    mess was pasted into challenge-02.txt

NOTES:
    http://www.pythonchallenge.com/pc/def/ocr.html  
    My idea is to create a dictionary with the count of each character
'''

dict1 = {}
i = 0

with open('challenge-02.txt', 'r') as fi:
    for line in fi:
        # print(line)
        for char in line:
            if char not in dict1:
                dict1[char] = 1
            else:
                i = dict1[char]
                i += 1
                dict1[char] = i

for char, count in dict1.items():
    print(f'{char}  {count}')

# RESULT:  http://www.pythonchallenge.com/pc/def/equality.html
# %  6104
# $  6046
# @  6157
# _  6112
# ^  6030
# #  6115
# )  6186
# &  6043
# !  6079
# +  6066
# ]  6152
# *  6034
# }  6105
# [  6108
# (  6154
# {  6046

#   1219
# e  1
# q  1
# u  1
# a  1
# l  1
# i  1
# t  1
# y  1