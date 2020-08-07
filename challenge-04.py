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

NOTES:
    view-source:http://www.pythonchallenge.com/pc/def/linkedlist.php

    <!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
        end. 400 times is more than enough. -->

    and the next nothing is 44827  (This message can be found when you click on the image)
    The url then changes to:
    http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345 
'''

import requests as req


fail = 'and the next nothing is'
r = 'and the next nothing is'
i = 0
# itter = 44827
itter = 8022
while fail in r:
    i += 1
    url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={itter}.php'
    print(url)
    rh = req.get(url)
    r = rh.text[0:300]
    if "Divide by two" in r:
        itter = itter/2
    else:
        itter = int("".join(filter(str.isdigit, r)))
    if i >= 400:
        print('did not work')
        break

if fail not in r:
    print(url)


#! http://www.pythonchallenge.com/pc/def/peak.html
# Result yeilded then I got this one in error on this page: http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044.php
# Yes. Divide by two and keep going.

# SO I divided 16044 by two == 8022 and restarted the script
# I also modified the script to auto do that next time.

#* It ran until it got by http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831.php 
# which rendered:
# peak.html 
# in the body.


# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44827.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=45439.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=94485.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=72198.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=80992.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8880.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=40961.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=58765.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=46561.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=13418.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=41954.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=46782.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=92730.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=89229.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=25646.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=74288.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=25945.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=39876.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8498.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=34684.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=62316.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=71331.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=59717.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=76893.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44091.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=73241.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=19242.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=17476.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=39566.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=81293.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=25857.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=74343.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=39410.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=5505.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=27104.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=54003.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=23501.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=21110.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=88399.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=49740.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=31552.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=39998.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=19755.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=64624.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=37817.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=43427.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=15115.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44327.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=7715.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=15248.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=61895.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=54759.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=54270.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=51332.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63481.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12362.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=94476.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=87810.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=6027.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=47551.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=79498.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=81226.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=4256.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=62734.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=25666.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=14781.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=21412.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=55205.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=65516.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=53535.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=4437.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=43442.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=91308.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=1312.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=36268.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=34289.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=46384.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=18097.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=9401.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=54249.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=29247.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=13115.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=23053.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=3875.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044.php