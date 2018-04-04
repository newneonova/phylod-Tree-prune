FASTA = 'fa.tmlblast.phylodb.fa'

UnsortedNames=list()
with open(FASTA) as F:
    for line in F:
        if line.startswith('>'):
            UnsortedNames.append(line)
UnsortedNames.sort()
open('SortedList.txt','w').write(''.join(UnsortedNames))

            
    
