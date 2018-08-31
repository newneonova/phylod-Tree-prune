RawFasta = "Combined_JCVI_NCBI_raw.fa"
OrderedHitTable = "SK76FMFH114-Alignment-HitTable.csv"

OrderedD = dict()

Temp=''
with open(RawFasta) as F:
    for line in F:
        if line.startswith('>'):
            Temp=line
        else:
            OrderedD[Temp.strip().replace('"','')[1:16]]=Temp+line
Outlines=list()
hitsHad=set()
OnlySixOTwo=list()
with open(OrderedHitTable) as F:
    for line in F:
        Name = line.split(',')[1].replace('"','')[:15]
        if Name in OrderedD:
            if Name not in hitsHad:
                Outlines.append(OrderedD[Name])
                hitsHad.add(Name)
                if len(OnlySixOTwo) < 602:
                    OnlySixOTwo.append(OrderedD[Name])

open('Combined_UNIQUE_ordered_by_eval_Total.fa','w').write(''.join(Outlines))

open('Combined_UNIQUE_ordered_by_eval_602.fa','w').write(''.join(OnlySixOTwo))
