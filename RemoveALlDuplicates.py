FASTA = 'Trimmed_Headers.fa'

OutLines = list()
KnownAminos = set()
Temp=''
TossedLine=list()
with open(FASTA) as F:
    for line in F:
        if line.startswith('>'):
            Temp=line
        else:
            if line not in KnownAminos:
                KnownAminos.add(line)
                OutLines.append(Temp)
                OutLines.append(line)
            else:
                TossedLine.append(Temp)
                TossedLine.append(line)
                      
            

open('Only_Unique_Aminos.fa','w').write(''.join(OutLines))
open('Redundant_Aminos.fa','w').write(''.join(TossedLine))
