#checking to see if any sequence is a subset of a different sequence.
# keeping only the longest

FASTA = 'Only_Unique_Aminos.fa'

dictionaryOfFasta = dict() #keyed by amino acids


OutLines = list()
KnownAminos = set()
Temp=''
TossedLine=list()
with open(FASTA) as F:
    for line in F:
        if line.startswith('>'):
            Temp=line
        else:
            dictionaryOfFasta[line]=Temp
            Temp=''

KeptList=list()
TossedList=list()
for key in dictionaryOfFasta.keys():
    keep=True
    for L in KeptList:
        if key in L:
            keep=False
            break
        if L in key:
            KeptList.remove(L)
            TossedList.append(L)
            break
    if keep == True:
        KeptList.append(key)
    else:
        TossedList.append(key)

Tossed=list()
for k in TossedList:
    Tossed.append(dictionaryOfFasta[k])
    Tossed.append(k)
open('Aminos_Contained_in_others.fa','w').write(''.join(Tossed))
Kept=list()
for k in KeptList:
    Kept.append(dictionaryOfFasta[k])
    Kept.append(k)
open('Unique_Longest.fa','w').write(''.join(Kept))


