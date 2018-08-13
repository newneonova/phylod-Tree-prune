HEADERS = 'TaxaResultsProcessed.txt'


Outlist = list()

BuiltLine=''

with open(HEADERS) as F:
    for line in F:
        I1= line.find(';')
        I2 = line[:I1].rfind(' ')
        lineK = line[I2:]
        Outlist.append(lineK)
            
        


open('TaxaResultsProcessed2.txt','w').write(''.join(Outlist))

