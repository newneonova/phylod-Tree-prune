import shutil, os
import re
FASTA = 'fa.tmlblast.phylodb.fa'
dir = 'FastasByAnnoShort'
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)
FastaFileById = dict()

Fasta = ''
CurID = ''

with open(FASTA) as F:
    for line in F:
        if line.startswith('>'):
            if CurID:
                if CurID not in FastaFileById:
                    FastaFileById[CurID]=list()
                FastaFileById[CurID].append(Fasta)
                CurID=''
                Fasta=''   
            CurID = line.split('ANNOTATION="')[1].split('"')[0].lower()[:20]
            Fasta=line
        else:
            Fasta+=line
    if CurID:
        if CurID not in FastaFileById:
            FastaFileById[CurID]=list()
        FastaFileById[CurID].append(Fasta)
        CurID=''
        Fasta=''   
for key,value in FastaFileById.items():
    open(dir+'/'+str(len(value))+'_'+re.sub('[^\w\-_\. ]', '_', key)+'.fa','w').write(''.join(value))


