import re
text = '''Die/ART Katze/N mag/V liebe/ADJ Mäuse/N ./SYM
Ich/PRO liebe/V Mäuse/N !/SYM'''
tokenTag = re.compile(r'(?:^|\s)(\S+)/(\S+)')
ttIndex = dict()
for match in tokenTag.finditer(text):
    if match.group(1) in ttIndex:
        ttIndex[match.group(1)].add(match.group(2))
    else:
        ttIndex[match.group(1)] = set()
        # sonst Laufzeitfehler!
        ttIndex[match.group(1)].add(match.group(2))


for (k,v) in ttIndex.items():
    print(k, "=>", v)
    
    


import pprint 
lexikon = {'Haus' :
{ 'genus' : 'neut',
'numerus' : 'sg',
'kasus': 'akk',
'val' : ['det','post gen'] } }

pprint.pprint(lexikon)