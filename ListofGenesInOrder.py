HEADERS = 'Only_Unique_processed_30Percent_sequence_blastp_JastHeaders.fa'


Outlist = list()


with open(HEADERS) as F:
    for line in F:
        Outlist.append(line.split('>')[1].split(' ')[0])

open('OrderedGenID.txt','w').write('\n'.join(Outlist))

