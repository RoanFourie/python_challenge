'''
Python v3.8 or later
Windows 10
For fun.
DESCRIPTION: Peak Hell
OWNER: Roan Fourie
REVISION: 0
REVISION DATE: 2020-06-12 (Week 24)
REVISION AUTHOR: Roan Fourie
REVISION DESCRIPTION:
    <!-- peak hell sounds familiar ? -->

NOTES:
    pronounce it

    view-source:http://www.pythonchallenge.com/pc/def/peak.html

    <!-- peak hell sounds familiar ? -->

    The image name was peakhell.jpg

    Peak Hell sounds like "pickle"

'''

#! www.pythonchallenge.com/pc/def/pickle.html
# Yields: yes! pickle!

# Could not find this one so I googled...
# https://www.hackingnote.com/en/python-challenge-solutions/level-5

from urllib.request import urlopen
import pickle

raw = urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()
raw.decode()

data = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

for line in data:
    print("".join([k * v for k, v in line]))


# Result: http://www.pythonchallenge.com/pc/def/channel.html

              #####                                                                      ##### 
               ####                                                                       ####
               ####                                                                       #### 
               ####                                                                       ####
               ####                                                                       ####
               ####                                                                       ####
               ####                                                                       ####
               ####                                                                       ####
      ###      ####   ###         ###       #####   ###    #####   ###          ###       ####
   ###   ##    #### #######     ##  ###      #### #######   #### #######     ###  ###     ####
  ###     ###  #####    ####   ###   ####    #####    ####  #####    ####   ###     ###   ####
 ###           ####     ####   ###    ###    ####     ####  ####     ####  ###      ####  ####
 ###           ####     ####          ###    ####     ####  ####     ####  ###       ###  ####
####           ####     ####     ##   ###    ####     ####  ####     #### ####       ###  ####
####           ####     ####   ##########    ####     ####  ####     #### ##############  ####
####           ####     ####  ###    ####    ####     ####  ####     #### ####            ####
####           ####     #### ####     ###    ####     ####  ####     #### ####            ####
 ###           ####     #### ####     ###    ####     ####  ####     ####  ###            ####
  ###      ##  ####     ####  ###    ####    ####     ####  ####     ####   ###      ##   ####
   ###    ##   ####     ####   ###########   ####     ####  ####     ####    ###    ##    ####
      ###     ######    #####    ##    #### ######    ###########    #####      ###      ######
