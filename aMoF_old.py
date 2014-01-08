#############################***********alec's Motif Finder***********############################
#                                                                                                #
# The aim of this software is to provide a full featured 'motif finder' focused on the analysis  #
# of typical APTAMER selection results. Aptamers are short sequence of nucleotides or aminoacids #
# (DNA, RNA, peptides, circular peptides and small proteins). In molecular biology, there are    #
# two main methods to select aptamers: SELEX and Phage Display. Both methods rely on the         #
# analysis of sequences to discriminate specifically enriched aptamers from background noise.    #
# The input of this software is then a list of short sequences of DNA, RNA or peptides.          #
# The lenght of such sequences is tipically in a range of 5 and 50 units. The sequences are      #
# composed exclusively by strings of alphabet characters.                                        #
#                                                                                                #
##################################################################################################







def merge_sequences(in_file, out_file):
	'''(input file name, output file name) -> dict of {'id':'sequence'}, ['merged_sequences'], output_file
	Read a fasta format and store its data in a dictionary with >name as key and sequence as value.
	Merge all the sequence lines of input_file into merged_sequences. 
	Write 'merged-sequences' into a file.
	Precondition: the file must be in fasta format.
	'''
	sequence_dict = {}
	merged_sequences = ''
	print('>>>sequence list from ' + in_file + '\n')
	with open(in_file, 'r') as in_file:
		line = in_file.readline()
		while line != '':
			if line != '\n':
				id = line[0:].strip()
				line = in_file.readline()
				sequence = line[0:].strip().upper()
				print(id + '\n' + sequence + '\n')
				merged_sequences = merged_sequences + sequence
				line = in_file.readline()
				if id not in sequence_dict:
					sequence_dict[id] = sequence
				else:
					sys.exit(str('File format error: ' + id + ' is not an unique sequence id.' + '\nPlease check the sequence file and try again.'))
			else:
				line = in_file.readline()
		print(separation_line)
		with open(out_file, 'w') as out_file:
			out_file.write(merged_sequences)
		print('>>>merged sequence' + '\n' + merged_sequences)
#****************END*OF*FUNCTION****************
	

def find_motifs(in_file, motif_len, repetition, out_file):
	'''(input file name, int, int, outpu file name ) -> dict of motif:repetition, sorted list of list of str:int 
	Generate motif of lenght -motif_lenght- out of a sequence,
	then check whether the motif are repepted -repetition- times into the sequence.
	Return a ordered list containing motif as key
	and the times it was found to be repeted into the sequence as value.
	'''
	import operator
	with open(in_file, 'r',) as in_file:
		s = in_file.readline()
		motif_dict = {}
		for i in range(len(s)-motif_len):
			motif = s[i:i+motif_len]
			if motif not in motif_dict:
				motif_dict[motif] = 0
			motif_dict[motif] += 1
		motif_dict = {k: v for k, v in motif_dict.iteritems() if v >= repetition}	
		sorted_list = sorted(motif_dict.iteritems(), key = operator.itemgetter(1), reverse = True)
	print('>>>detected motifs')
	print(sorted_list)
	with open(out_file, 'w') as out_file_2:
			out_file_2.write(str(sorted_list))
#****************END*OF*FUNCTION****************


def find_motifs_3(in_file, motif_len, repetition, out_file): # Python 3 version
	'''(input file name, int, int, outpu file name ) -> dict of motif:repetition, sorted list of list of str:int 
	Generate motif of lenght -motif_lenght- out of a sequence,
	then check whether the motif are repepted -repetition- times into the sequence.
	Return a ordered list containing motif as key
	and the times it was found to be repeted into the sequence as value.
	'''
	import operator
	with open(in_file, 'r',) as in_file:
		s = in_file.readline()
		motif_dict = {}
		for i in range(len(s)-motif_len):
			motif = s[i:i+motif_len]
			if motif not in motif_dict:
				motif_dict[motif] = 0
			motif_dict[motif] += 1
		motif_dict = {k: v for k, v in motif_dict.items() if v >= repetition}	
		sorted_list = sorted(motif_dict.items(), key = operator.itemgetter(1), reverse = True)
	print('>>>detected motifs')
	print(sorted_list)
	with open(out_file, 'w') as out_file_2:
			out_file_2.write(str(sorted_list))
#****************END*OF*FUNCTION****************


def hist_report(in_file, motif_len):
	'''(input file name, int)-> str
	Take a file with 'merged_sequences' as input and makes a histogram-like report of the most repeated motifs.
	'''
	letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
	num = '0123456789'
	with open(out_file_2, 'r') as in_file:
		line = in_file.readline()
		n = 0
		top_10 = 0
		print('>>>top_10')
		while n < len(line) and top_10 < 10:
			if line[n] not in letters and line[n] not in num:
				n += 1
			elif line[n] in letters:
				motif = line[n:n+motif_len]
				n += motif_len
			else:
				repeated = ''
				while line[n] in num:
					repeated += line[n]
					n += 1
				print(motif + ' :' + '*'*int(repeated))
				top_10 += 1
#****************END*OF*FUNCTION****************	


#######alecMotifFinderTEST#######
#variables
motif_len = 5
repetition = 4
write_to_log = 'no' #if yes, it prints the output in log.txt instead printing on screen

#files
in_file = 'sequence_file.txt'
out_file_1 = 'out_file_1.txt'
out_file_2 = 'out_file_2.txt'

#gui
separation_line ='\n#######################################\n'
app_title = '***********Alec Motif Finder***********'
version = 'alpha - December 2013'
credits = 'by alec_djinn@yahoo.com'

#imports
import sys
import time

#log part 1
if write_to_log == 'yes':
	old_stdout = sys.stdout
	log_file = open('log.txt','w') # change to open('log.txt','a') to append consecutive run on log.txt
	sys.stdout = log_file
else:
	pass
	
#body
start_time = time.time()
print('\n')
print(app_title)
print('\n' + 'version :' + version)
print(credits)
print ('\n' + 'date : ' + time.strftime("%d/%m/%Y") + '   time : ' + time.strftime("%H:%M:%S"))
print(separation_line)
merge_sequences(in_file, out_file_1)
print(separation_line)
version_check = int((sys.version)[0]) # check Python version
if version_check == 2:
	# execute code for Python 2
	print('Detected Python 2')
	find_motifs(out_file_1, motif_len, repetition, out_file_2)
elif version_check == 3:
	#execute code for Python 3
	print('Detected Python 3')
	find_motifs_3(out_file_1, motif_len, repetition, out_file_2)
else:
	sys.exit('Python version error, please execute this orogram using Python version 2.7.x or newer')
print(separation_line)
hist_report(in_file, motif_len)
print(separation_line)
print('execution time')
print(str(time.time() - start_time) + ' seconds\n')

#log part 2
if write_to_log == 'yes':
	sys.stdout = old_stdout #log END
	log_file.close() #close log_file
	sys.exit('program ran succesfully and its output has been written in log.txt')
else:
	pass 

#exit
sys.exit('program ran succesfully')



