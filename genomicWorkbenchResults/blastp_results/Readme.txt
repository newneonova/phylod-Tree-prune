Using NCBI Genome Workbench

Imported the fa.tmlblast.phylodb.fa sequences (4211 components)

Ran blast using the Phatr11014-4Phatr2 TAXID="2850" as the query sequence and all 4211 sequences of fa.tmlblast.phylodb.fa as the target sequences.

Ran using the default general parameters (word size = 3, e-value = 10, Threshold = 11, though changing these to 3,1,1, and 3,10000,10000 did not change the result, 3-1-1 resulted in 506 sequences, and 3,10000,10000 in 515).

Exported the whole sequence results in 506 fasta sequences. Exporting unique locations results in 1108 fasta sequences (multiple sequences corrosponding to the original sequences based on how the alignment hook out. FOr instance there are 104 different ways that the target sequence aligns with itself listed in this file)