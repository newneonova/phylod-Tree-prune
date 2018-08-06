#checking to see if any sequence is a subset of a different sequence.
# keeping only the longest

rawFile = 'raw_outtable.txt'

resLines = list()
count=0
L=''
with open(rawFile) as F:
    for line in F:
        if(count==2):
            resLines.append(L+line)
            L=''
            count=0
        else:
            count=count+1
            L=L+line.replace('\n','\t')

open('processedTable.txt','w').write(''.join(resLines))


