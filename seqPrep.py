# The aim of this program is to prepare a list of sequences to serve as input to aMoF.
# The program takes as input a folder containing .fas files (crude sequencing results).
# It allows to discriminate Phage Display sequences from SELEX one.
# In case of Phage Display the kind of library that has been used can be chosen (PhD12. PhDC7C, etc...)
# In case of SELEX you can indicate the sequencing primer and the sequences flag regions

# FUNCTIONS
def chooseExperiment():
	global exp_list
	global experiment_type
	exp_list = [1,2,3,4,5]
	print('*******************************')
	print('Phage Display using PhD-12  : 1')
	print('Phage Display using PhD-7   : 2')
	print('Phage Display using PhD-C7C : 3')
	print('M13 - p8 N-term display     : 4')
	print('DNA SELEX                   : 5')
	print('RNA SELEX                   : 6')
	print('*******************************')
	experiment_type = int(input('Please indicate from which experiment are the input sequences coming from...'))
	return experiment_type


def translateDNA(sequence, experiment_type):
	gencode = {
    	'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    	'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    	'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    	'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    	'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    	'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    	'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    	'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    	}
<<<<<<< HEAD

	# if amber mutant
	if experiment_type == 1 or 2 or 3 or 4:
		gencode['TAG'] = 'Q'

=======
	
	# if amber mutant
	if experiment_type == 1 or 2 or 3 or 4:
		gencode['TAG'] = 'Q'
	
>>>>>>> FETCH_HEAD
	proteinseq = ''
	for n in range(0,len(sequence),3):
		if gencode.has_key(sequence[n:n+3]) == True:
			proteinseq += gencode[sequence[n:n+3]]
		else:
			proteinseq += '#'	
	return proteinseq


def reverseComplement(input_sequence):
	reverse_complement = ''
	n = len(input_sequence)-1
	while n >= 0:
		if input_sequence[n] == 'A':
			reverse_complement += 'T'
			n -= 1
		elif input_sequence[n] == 'T':
			reverse_complement += 'A'
			n -= 1
		elif input_sequence[n] == 'C':
			reverse_complement += 'G'
			n -= 1
		elif input_sequence[n] == 'G':
			reverse_complement += 'C'
			n -= 1
		else:
			reverse_complement += 'N'
			n -= 1
	return reverse_complement


def concatenateFAS(folder, outfilename):
	'''(path, outfilename) -> outfile
	Combine the content of all files .fas founded in a specific folder into a file.
	Precondition: the folder must be in the same main-folder of the script. 
	'''
	with open(outfilename, 'wb') as outfile:
		for filename in glob.glob(folder + '*.fas'):
			with open(filename) as readfile:
				shutil.copyfileobj(readfile, outfile)


def formatSequences(infile, experiment_type):
	'''(input file name) -> str
	Reads a file containing a list of sequences preceded by a unique sequence id.
	Removes all unneeded blank lines and checks whether the id is unique.
	Prints the list of sequences found in the file.
	Precondition: each sequence in the file is above its id. 
	'''
	sequence_dict = {}
	corrupted_list = []
	unreadable_list = []
	wildtype_list = []
	count = 0
	wildtype = 0
	corrupted = 0
	unreadable = 0
	print('>>>sequences found in ' + infile + ' formatted by experiment type ' + str(experiment_type) + '\n')
	with open(infile, 'r') as infile:
		line = infile.readline()
		while line != '':
			if line != '\n' and line[0:3] != '>>>': # skip initial blank lines and '>>>' tagged lines
<<<<<<< HEAD

=======
				
>>>>>>> FETCH_HEAD
				# check for a valid FASTA id
				if line[0:1] == '>':
					id = line[0:9] + '-' + line[31:34].upper() # keep only the seq ID values
					count += 1
					line = infile.readline()
<<<<<<< HEAD

				# check for a valid FASTA sequence after the ID line
				if line[0:1] != '>':
					sequence = line[0:].strip().upper()

=======
				
				# check for a valid FASTA sequence after the ID line
				if line[0:1] != '>':
					sequence = line[0:].strip().upper()
									
>>>>>>> FETCH_HEAD
				# if PhD-C7C
				if experiment_type == 3:
					left_flank = 'GTGGTACCTTTCTATTCTCACTCTGCTTGT'
					right_flank = 'TGCGGTGGAGGTTCGGCCGAAACTGTT'
					wild_type = 'GTACCTTTCTATTCTCACTCGGCCGAAACTGTTGAAAGTTGTTTAGCAAAA'
<<<<<<< HEAD

=======
					
>>>>>>> FETCH_HEAD
				# if M13 - p8 N-term display
				if experiment_type == 4:
					left_flank = 'TTCCGATGCTGTCTTTCGCT'
					right_flank = 'GCTGAGGGTGACGATCCCGCAAA'
					wild_type = 'GTCTTTCGCTGCTGAGGGTGACGATCCCGCAAAAG'
<<<<<<< HEAD

=======
					
>>>>>>> FETCH_HEAD
				sequence = reverseComplement(sequence)										
				if wild_type in sequence:
					wildtype += 1
					wildtype_list += [id]
				elif left_flank and right_flank in sequence:
					sequence = sequence[sequence.rfind(left_flank)+len(left_flank):sequence.rfind(right_flank)]
					sequence = translateDNA(sequence, experiment_type)
					print(id + '\n' + sequence + '\n')
					if '#' in sequence:
						corrupted += 1
						corrupted_list += [id]
				else:
					unreadable += 1
					unreadable_list += [id]
<<<<<<< HEAD

=======
						
>>>>>>> FETCH_HEAD
				line = infile.readline()
				if id not in sequence_dict: #check if the id are unique
					sequence_dict[id] = sequence			
				else:
					sys.exit(str('File format error: ' + id + ' is not an unique sequence id.' + '\nPlease check the sequence file and try again.'))
			else:
				line = infile.readline()
	print('>>>Total sequences  : ' + str(count))
	print('>>>Unreadable       : ' + str(unreadable)) + ' --> ' + str(unreadable_list)
	print('>>>Corrupted        : ' + str(corrupted)) + ' --> ' + str(corrupted_list)
	print('>>>Wild Type        : ' + str(wildtype)) + ' --> ' + str(wildtype_list)
	print('>>>Good             : ' + str(count - (corrupted + wildtype + unreadable)))
<<<<<<< HEAD


# BEGINNING

=======
	
	
# BEGINNING

>>>>>>> FETCH_HEAD
# imports
import sys
import time
import shutil
import glob

# variables
folder = 'FASfiles/'            	
outfilename = 'all_sequences.txt'
infile = outfilename
old_stdout = ''

# check user input
chooseExperiment()
while experiment_type not in exp_list:
	print('\n\n****   ERROR! ' + str(experiment_type) + ' is not a valid choice. Please try again...   ****\n\n')
	chooseExperiment()
<<<<<<< HEAD

=======
		
>>>>>>> FETCH_HEAD
# write output - part 1
write_to_log = 'yes' # if yes, it prints the output in FAS_log.txt instead printing on screen
logfile = 'FAS_log.txt'
logfilename = logfile
if write_to_log == 'yes':
	old_stdout = sys.stdout
	logfile = open(logfile,'w')
	sys.stdout = logfile
else:
	pass
<<<<<<< HEAD

=======
	
>>>>>>> FETCH_HEAD
# body
start_time = time.time()
concatenateFAS(folder, outfilename)
formatSequences(infile, experiment_type)
print('>>>execution time :' + str(time.time() - start_time) + ' seconds\n')

# write output - part 2
if write_to_log == 'no':
	sys.stdout = old_stdout #log END
	logfile.close() # close log_file
	# exit
	sys.exit('program ran succesfully and its output has been written in ' + logfilename)
else:
	pass
<<<<<<< HEAD

# exit
sys.exit('program ran succesfully')
=======
	
# exit
sys.exit('program ran succesfully')
>>>>>>> FETCH_HEAD
