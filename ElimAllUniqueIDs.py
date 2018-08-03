FASTA = 'REVISED_MASTERFILE.fa'

OutLines = list()

with open(FASTA) as F:
    for line in F:
        if line.startswith('>'):
            Sindex = 6
            Eindex = line.index("TAXONOMY=")+9
            
            Tline = line[:Sindex]+line[Eindex:]
            NUMS=Tline[:6]
            ENDS=Tline[6:].split(';')
            keep=list()
            counter=0
            if ENDS[len(ENDS)-1].startswith(ENDS[len(ENDS)-2]):
                ENDS[len(ENDS)-2]=''
                
            for i in ENDS:
                if not i.endswith('_X') and not i.endswith('_XX'):
                    keep.append(i)
                else:
                    keep.append('')                
            OutLines.append(NUMS+';'.join(keep))
        else:
            OutLines.append(line)
                      
            

open('Trimmed_Headers.fa','w').write(''.join(OutLines))
