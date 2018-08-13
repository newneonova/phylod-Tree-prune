HEADERS = 'TaxaResultsRaw.txt'


Outlist = list()

BuiltLine=''
done=False
with open(HEADERS) as F:
    for line in F:
        if not done and not '*-*-' in line:
            if 'COMMENT' in line:
                done=True
            else:
                BuiltLine=BuiltLine+line.rstrip()



        if '*-*-' in line:
            
            done=False
            Outlist.append(BuiltLine)
            BuiltLine=''
            NumInBlock = 0

            
            
        


open('TaxaResultsProcessed.txt','w').write('\n'.join(Outlist))

