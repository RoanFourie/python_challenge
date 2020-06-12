'''
Python v3.8 or later
Windows 10
For fun.
DESCRIPTION: Decrypt the message.
OWNER: Roan Fourie
REVISION: 0
REVISION DATE: 2020-06-12 (Week 24)
REVISION AUTHOR: Roan Fourie
REVISION DESCRIPTION:
    K -> M  
    O -> Q  
    E -> G  
    g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.  
NOTES:
    http://www.pythonchallenge.com/pc/def/map.html  
'''

trans = str.maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab")
message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(message.translate(trans))

# Result: i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient 
# and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
print('map'.translate(trans))  # == ocr

# http://www.pythonchallenge.com/pc/def/ocr.html
