import shutil, os
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
WinLen=0

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
            CurID = line.split('ANNOTATION="')[1].split('"')[0].lower()[:20]
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
    #if len(value)>0:
        #FinalFastaList.append(value.pop())

open('LongestFastaPerAnnotation'+str(len(FinalFastaList))+'.fa','w').write(''.join(FinalFastaList))


