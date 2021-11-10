from colorize import *
from random import choice as rand

practice_dict_0 = {
'text1': 561,
'text2': 943,
'text3': 643,
'text4': 846,
'text5': 235,
'text6': 264,
'text7': 673,
'text8': 483,
'text9': 351,
'text0': 287,
'text11': 39,
'text12': 48,
'text13': 90,
'text14': 86,
'text15': 23,
'text16': 64,
'text17': 67,
'text18': 48,
'text19': 51,
'text10': 87,
}

def sample(dictionary, target, precision, master_dict, added='INIT', SUM=0, ret={}):
    margin = (int(target - (target * precision)), int(target + (target * precision)))
    dictionary = dictionary.copy()

    if added == 'INIT':
        added = []

    if SUM in range(margin[0], margin[1] + 1):
        printc(SUM, 'yellow')
        printc(added, 'green')
        if SUM not in ret:
            ret[SUM] = [added]
        else:
            ret[SUM].append(added)
        return ret
    
    elif SUM > target:
        # printc(SUM, 'red')
        added.pop(-1)
        return ret

    elif dictionary == {}:
        return ret

    while(len(dictionary.keys()) > 0):
        item = rand(list(dictionary.keys()))
        if item not in added:
            added.append(item)
            SUM = sum([v if k in added else 0 for k,v in master_dict.items()])
            del dictionary[item]

            ret = sample(dictionary, target, precision, master_dict, added, SUM, ret)
        
        else:
            del dictionary[item]

for i in range(len(list(practice_dict_0.keys()))):
    ret = sample(practice_dict_0, 1000, .02, practice_dict_0.copy())

pause = 1
