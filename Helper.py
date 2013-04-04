import collections
from itertools import islice

def PrintDict(dict,number, title):
    print "=============================="
    print title
    print "=============================="
    sorted_dict = sorted(dict, key=dict.get, reverse=True)
    length = number
    if length > len(sorted_dict):
        length = len(sorted_dict)
    for i in range(0,length):
        item = sorted_dict[i]
        value = dict.get(item)
        print '{1:15d} \t {0}'.format(item,value)
        
def PrintTop10(dict,title):
    PrintDict(dict,10,title)
        
def PrintAll(dict,title):
    PrintDict(dict,len(dict),title)
    
def take(n, iterable):
    return list(islice(iterable,n))
    
def AddToDict(element,dict):
    if not (element in dict.keys()):
        dict[element] = 1
    else:
        dict[element] = dict[element] + 1

def DeleteLeadingZerosFromIP(ip):
    linesplit = ip.split('.')
    retvalue = ""
    for element in linesplit:
        retvalue = retvalue + element.lstrip('0') + "."
    return retvalue.rstrip('.')