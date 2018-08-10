FASTA = 'processed_30Percent_sequence_blastp.fa'
Fname = FASTA.split('.fa')[0]

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
open('Redundant_Aminos_'+Fname+'.fa','w').write(''.join(Tossed))
Kept=list()
for k in KeptList:
    Kept.append(dictionaryOfFasta[k])
    Kept.append(k)

open('Only_Unique_'+Fname+'.fa','w').write(''.join(Kept))

