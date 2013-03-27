import collections
from itertools import islice

def PrintTop10(dict, title):
    print "=============================="
    print title
    print "=============================="
    sorted_dict = sorted(dict, key=dict.get, reverse=True)
    length = 10
    if length > len(sorted_dict):
        length = len(sorted_dict)
    for i in range(0,length):
        item = sorted_dict[i]
        value = dict.get(item)
        print '{2:2d}.  {1:15d} \t {0}'.format(item,value,i+1)
        
def take(n, iterable):
    return list(islice(iterable,n))
    
def AddToDict(element,dict):
    if not (element in dict.keys()):
        dict[element] = 1
    else:
        dict[element] = dict[element] + 1