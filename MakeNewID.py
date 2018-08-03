FASTA = 'fa.tmlblast.phylodb.fa'

OutLines = list()
ID = 1;

with open(FASTA) as F:
    for line in F:
        if line.startswith('>'):
            OutLines.append(line.replace('>','>'+format(ID,'04')+'_'))
            ID=ID+1
        else:
            OutLines.append(line)
                      
            

open('NEW_ID_fa.tmlblast.phylodb.fa','w').write(''.join(OutLines))
