aMoF - aptamers Motif Finder
====
aMoF is a collection of Python scripts developed to to provide a full featured 'motif finder' tools focused on the analysis of APTAMERS selection results.
Classical motifs (or kmers) findinding tools take as input long bio-sequences like entire genomes or sets of genes.  aMoF instead, focuses on sets of short sequences that are the tipical results of an aptamer selection experiment.
aMoF is ment to be user friendly and "dummy proof" so the code is compatible with both Python2 and Python3 and it relies ONLY on the Python Standard Library.


##Some background information
Aptamers are short sequence of nucleotides or aminoacids (DNA, RNA, peptides, circular peptides and small proteins) that bind to a specific target molecule.
They can be used for both basic research and clinical purposes as macromolecular drugs or as "atibody-like-particles" for molecular detection.
Aptamers are naturalli present in living organisms where they often act as switch to regulate many different pathways.
In molecular biology, there are two main methods to select aptamers: SELEX and Phage Display. Both methods rely on the analysis of sequences to discriminate specifically enriched aptamers from background noise.

To know more about aptamers here are some links ;)
* http://en.wikipedia.org/wiki/Aptamer
* http://en.wikipedia.org/wiki/Riboswitch
* http://en.wikipedia.org/wiki/Phage_display
* http://en.wikipedia.org/wiki/Systematic_Evolution_of_Ligands_by_Exponential_Enrichment


##Disclaimer
Since I am not a professional programmers you may find the code structure "not conventional", you are free to comment on it and suggest improvements. 


##Overview and How-To-Use info
#####aMoF.py
It is the core program.
It contains the "motifs finder" algorithm and the variables indicating the input the output files.

#####seqPrep.py
This program prepare an appropriate formatted file to serve as input to aMof.py .
It reads all the fas files (obtained by sequencing) contained in the folder FASfiles and it extracts each sequence and the relative id and writes them in a file.
This program allow the user to better define from which kind of selection experiment the sequences are coming from.

You can chose among this type of experiments:
* M13 Phage Display usinf PhD-12
* M13 Phage Display usinf PhD-7
* M13 Phage Display usinf PhD-C7C
* T7 Phage Display
* Ribosome Display
* DNA SELEX
* RNA SELEX

With this information program will automatically slice out the sequence of interest from the whole sequencing result and it translate it if needed.
For example, in case of M13 Phage Display usinf PhD-C7C, a classic sequencing output, using company provided sequencing primers, looks like this:
* >12826357.seq - ID: CB8 - Phage Display - PhDC7C - Acid Elution 3 - Plate 2_A01-Amply M13 pIII CS - R on 2014/1/16-0:53:50 automatically edited with PhredPhrap, start with base no.: 41  Internal Params: Windowsize: 20, Goodqual: 19, Badqual: 10, Minseqlength: 50, nbadelimit: 1
* agTTTTgTCGTCTTTcCagACGTTAGTAAATGAATTTTCtGtAtGGgattTTGCTAAACAACTTTCAACAGTTTCGGCCGAACCTCCACCGCACTCATAAGGCGAACCAGTATTACAAGCAGAGTGAGAATAGAAAGGTACCACTAAAGGAATTGCGAATAATAATTTTTTCACGTTGAAAATCTCCAAAAAAAAGGCTCCAAAAGGAGCCTTTAATTGTATCGGTTTATCAGCTTGCTTTCGAGGTGAATTTCTTAAACAGCTTGATACCGATAGTTGCGCCgACnATGACAACAACCATCGCCCACGCATAACCGATATATTCGGTCGCTGAGGCTTGCAGGGAGTTAAAGGCCGCTTTTGCGGGATCGTCACCCTCAGCAGCGAaagAcAGCATCGGAACGAGGGTAGCAACGGCTACAGAGGCTTTGAGGACTAAAGACTTTTTCATGAGGAAGTTTCCATTAAACGGGTAAAATACgTAATGCCACTACGAAGGCACCaaCCTAAAACgAaagAGGCAaaanAATACactAaaACACTCATCTTTGACCCCCAgcGATTATACCAAGCGCGAAACAAAGtACAACGGAGATTTGTATCATCGCCTGATAAATTGTGTCgAAnTCCGCGAcCTGCTCCATGTTACTTAgCCGGAACGAGGCGCAGACGGnCAATcannnnGGAaCCGAaCTGACCaACtTTGAAAgAggacnnAngAaCGGTGTACAGACCAGGCGCATAGGCTGGCTGAnCtTtCaTcaAnAgtAnnctTGAcAAGAACCGGATATTCATTAcCCnAAnTCaacGtACnaAGCTnGCtCaTTccannGAAnnAAGGctTGcCCTGAcgAgAAACacCananngAgtAGTAAATTGGgcTTtGAgATGgnnttattTCaaCTTTaatCaTTGTGAATTACcttntGCgAtTTnanAAcTGGCTcatta

and after using seqPrep.py it looks like this:
* >12826357-A01
* NTGSPYE

Note that the repeated sequence at N-ter (AC) and C-term (CGGGS), distinctive of any PhD-C7C sequence, has been sliced out to exclude them from future statistical analysis 






                                       
