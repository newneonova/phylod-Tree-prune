import shutil, os
import re
FASTA = 'fa.tmlblast.phylodb.fa'
#dir = 'FastasByTax'
#if os.path.exists(dir):
#    shutil.rmtree(dir)
#os.makedirs(dir)

#OK trying some tossout rules
# toss any sequence whose Fasta part is fewer than 70 characters
# if we have multiple sequences of the same ID, keep only the longest 2

FastaFileById = dict()

Fasta = ''
CurID = ''
FastaPart = ''
WinLen=200

with open(FASTA) as F:
    for line in F:
        if line.startswith('>'):
            if CurID:
                if len(FastaPart)>WinLen:
                    if CurID not in FastaFileById:
                        FastaFileById[CurID]=list()
                    FastaFileById[CurID].append(Fasta)
                CurID=''
                Fasta=''
                FastaPart=''
            TempID = line.split('TAXONOMY="')[1].split('"')[0]
            Arr = TempID.split(';')
            CurID = Arr[4]
            re.sub('[^\w\-_\. ]', '_', CurID)
            CurID= CurID.replace(r'/','_')
            CurID= CurID.replace(r'*','_')
            CurID= CurID.replace(r'.','_')
            CurID= CurID.replace(r':','_')
            Fasta=line
        else:
            FastaPart+=line.strip();
            Fasta+=line
    if CurID:
        if len(FastaPart)>WinLen:
            if CurID not in FastaFileById:
                        FastaFileById[CurID]=list()
                        FastaFileById[CurID].append(Fasta)
            FastaFileById[CurID].append(Fasta)
        CurID=''
        Fasta=''
FinalFastaList=list()
for key,value in FastaFileById.items():
    value.sort(key=len)
    FinalFastaList.append(value.pop())
#    if len(value)>0:
#        FinalFastaList.append(value.pop())

open('1Per5thEntry'+str(len(FinalFastaList))+'.fa','w').write(''.join(FinalFastaList))


