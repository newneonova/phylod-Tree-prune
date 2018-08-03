import shutil, os
import re
FASTA = 'fa.tmlblast.phylodb.fa'
dir = 'FastasBytaxonomy4'
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
            Fasta+=line
    if CurID:
        if CurID not in FastaFileById:
            FastaFileById[CurID]=list()
        FastaFileById[CurID].append(Fasta)
        CurID=''
        Fasta=''   
for key,value in FastaFileById.items():
    open(dir+'/'+str(len(value))+'_'+key+'.fa','w').write(''.join(value))


