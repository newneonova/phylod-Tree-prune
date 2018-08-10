#checking to see if any sequence is a subset of a different sequence.
# keeping only the longest

rawFile = '20000_sequence_blastp.fa'

resLines = list()
H=''
L=''
with open(rawFile) as F:
    for line in F:
        if line.startswith('>'):
            if H!='':
               resLines.append(H)
               resLines.append(L+'\n')
               L=''
            H=line
        else:
            L=L+line.replace('\n','')
resLines.append(H)
resLines.append(L)
open('processed_'+rawFile,'w').write(''.join(resLines))


