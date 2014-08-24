#imports	
import operator
import sys
import time

#functions
def formatSequences(infile):
	'''(input file name) -> str
	Reads a file containing a list of sequences preceded by a unique sequence id.
	Removes all unneeded blank lines and checks whether the id is unique.
	Prints the list of sequences found in the file.
	Precondition: each sequence in the file is above its id. 
	'''
	sequence_dict = {}
	count = 0
	print('>>>sequences found in file ' + infile + '\n')
	with open(infile, 'r') as infile:
		line = infile.readline()
		while line != '':
			if line != '\n' and '>>>' not in line: #skip initial blank lines and '>>>' tagged lines
				id = line[0:].strip().upper()
				#count += 1
				line = infile.readline()
				while line == '\n' or '>>>' in line: #skip blank and '>>>' tagged lines between id and sequence
					line = infile.readline()
				sequence = line[0:].strip().upper()
				if sequence != 'WILD TYPE' and sequence != 'CORRUPTED':
					print(id + '\n' + sequence + '\n')
					count += 1
				line = infile.readline()
				if id not in sequence_dict: #check if the id are unique
					sequence_dict[id] = sequence
				else:
					sys.exit(str('File format error: ' + id + ' is not an unique sequence id.' + '\nPlease check the sequence file and try again.'))
			else:
				line = infile.readline()
	print('>>>total sequences found ' + str(count) + '\n')			

def findMotifs(infile, motif_len, repetition):
	'''(input file name, int, int) -> sorted dictionary
	Reads a file containing a list of sequences preceded by a unique sequence id.
	Removes all unneeded blank lines and checks whether the id is unique.
	Generates a dictionary of id, motifs.
	Evaluates whether a motif is repeated at least 'repetition' times -> if not, deletes it from the dictionary.
	Sorts the dictionary and prints a report.
	Precondition: each sequence in the file is above its id. 
	'''
	#sequence_dict = {}
	motif_dict = {}
	with open(infile, 'r') as infile:
		line = infile.readline()
		while line != '':
			if line != '\n' and '>>>' not in line: #skip initial blank lines and '>>>' tagged lines
				id = line[0:].strip().lower() #set id in lowercase
				line = infile.readline()
				while line == '\n' or '>>>' in line: #skip blank and '>>>' tagged lines between id and sequence
					line = infile.readline()	
				sequence = line[0:].strip().upper()	#set sequence in uppercase
				#print(id + '\n' + sequence + '\n')
				for i in range(len(sequence) - motif_len +1): #generate a dictionary of motifs (motif_dict)
					motif = sequence[i:i+motif_len]
					if motif not in motif_dict:
						motif_dict[motif] = 1
					else:
						motif_dict[motif] += 1
				line = infile.readline()
				#if id not in sequence_dict:
					#sequence_dict[id] = sequence
				#else:
					#sys.exit(str('File format error: ' + id + ' is not an unique sequence id.' + '\nPlease check the sequence file and try again.'))
			else:
				line = infile.readline()
	#remove from motif_dict all the motif repeated less than 'repetition' times
	keys_to_remove = [key for key, value in motif_dict.items() if value < repetition]
	for key in keys_to_remove:
		del motif_dict[key]
	#sort the dictionary
	global sorted_list #set sorted_list as global variable
	sorted_list = sorted(motif_dict.items(), key = operator.itemgetter(1), reverse = True)
	print('>>>detected motifs with lenght = ' + str(motif_len) + ' and repeated at least ' + str(repetition) + ' times')
	print(sorted_list)
	print('\n')			

def main(infile='FAS_log.txt', motif_len_=1, repetition_=3, write_to_log='yes', logfile='results_b.txt'):
	global motif_len, repetition, sorted_list
	motif_len = motif_len_
	repetition = repetition_
	#write output - part 1
	if write_to_log == 'yes':
		old_stdout = sys.stdout
		log_file = open(logfile,'w')
		sys.stdout = log_file
	else:
		pass

	#body
	start_time = time.time()
	formatSequences(infile)
	sorted_list = [1]
	while sorted_list != []:
		findMotifs(infile, motif_len, repetition)
		motif_len += 1

	print('>>>execution time :' + str(time.time() - start_time) + ' seconds\n')

	#write output - part 2
	if write_to_log == 'yes':
		sys.stdout = old_stdout #log END
		log_file.close() #close log_file
		#exit
		sys.exit('>>>program ran succesfully and its output has been written in ' + logfile)
	else:
		pass
	
	#exit
	sys.exit('>>>program ran succesfully')
	
if __name__ == '__main__':
    main()
    
