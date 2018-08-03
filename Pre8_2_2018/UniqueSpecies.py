FASTA = 'LongestFastaPerAnnotation237.fa'

UnsortedNames=list()
TaxID = set()
with open(FASTA) as F:
    for line in F:
        if line.startswith('>'):
            UnsortedNames.append(line)
            TaxID.add(line.split('SPECIES="')[1].split('"')[0])
                      
print(str(len(UnsortedNames))+" "+str(len(TaxID)))                    
#UnsortedNames.sort()
#open('SortedList.txt','w').write(''.join(UnsortedNames))
