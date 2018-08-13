Fastas = 'Only_Unique_processed_30Percent_sequence_blastp.fa'
TaxaInfo = 'TaxaResultsProcessed2.txt'

Outlist = list()
count=0

OrderedTaxas=list()
with open(TaxaInfo) as F:
    for line in F:
        OrderedTaxas.append(line)

hadLine=''
with open(Fastas) as F:
    for line in F:
        if line.startswith('>'):
            count=count+1
            hadLine=line[:1]+str(count).zfill(5)+"_"+line[1:].rstrip()+" "+OrderedTaxas[count-1]
        else:
            hadLine=hadLine+line
            Outlist.append(hadLine)
            hadLine=''



open('processed_30Percent_sequence_blastp_With_Taxa.fa','w').write(''.join(Outlist))

