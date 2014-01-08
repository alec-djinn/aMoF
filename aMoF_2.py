def check_python():
	'''(none) -> str
	It checks Python version (only the major int) and prints what has been found. 
	'''
	version_check = int((sys.version)[0]) # checks Python version
	if version_check == 2:
		# executes code for Python 2
		print('Detected Python 2')
	elif version_check == 3:
		# executes code for Python 2
		print('Detected Python 3')
	else:
		sys.exit('Python version error!!\nThis program is compatible not compatible with your Python version.\nPlease install Python 2.7.x or Python 3.x')		
#****************END*OF*FUNCTION****************


def format_sequences(infile):
	'''(input file name) -> str
	Reads a file containing a list of sequences preceded by a unique sequence id.
	Removes all unneeded blank lines and checks whether the id is unique.
	Prints the list of sequences found in the file.
	Precondition: each sequence in the file is above its id. 
	'''
	sequence_dict = {}
	print('>>>sequences found in file ' + infile + '\n')
	with open(infile, 'r') as infile:
		line = infile.readline()
		while line != '':
			if line != '\n': # skips initial blank lines
				id = line[0:].strip().lower()
				line = infile.readline()
				while line == '\n': # skips blank lines between id and sequence
					line = infile.readline()
				sequence = line[0:].strip().upper()
				print(id + '\n' + sequence + '\n')
				line = infile.readline()
				if id not in sequence_dict: # checks if the id are unique
					sequence_dict[id] = sequence
				else:
					sys.exit(str('File format error: ' + id + ' is not an unique sequence id.' + '\nPlease check the sequence file and try again.'))
			else:
				line = infile.readline()			
#****************END*OF*FUNCTION****************


def find_motifs(infile, motif_len, repetition):
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
			if line != '\n':
				id = line[0:].strip().lower() # set id in lowercase
				line = infile.readline()
				while line == '\n':
					line = infile.readline()	
				sequence = line[0:].strip().upper()	# set sequence in uppercase
				#print(id + '\n' + sequence + '\n')
				for i in range(len(sequence) - motif_len +1): # generates a dictionary of motifs (motif_dict)
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
	# removes from motif_dict all the motif repeated less than 'repetition' times
	keys_to_remove = [key for key, value in motif_dict.items() if value < repetition]
	for key in keys_to_remove:
		del motif_dict[key]
	# sorts the dictionary
	global sorted_list # sets sorted_list as global variable
	sorted_list = sorted(motif_dict.items(), key = operator.itemgetter(1), reverse = True)
	print('>>>detected motifs with lenght = ' + str(motif_len) + ' and repeated at least ' + str(repetition) + ' times')
	print(sorted_list)
	print('\n')			
#****************END*OF*FUNCTION****************


# import	
import operator
import sys
import time

# variables
start_time = time.time()
infile = 'sequence_file.txt'
motif_len = 5
repetition = 4
sorted_list = [1]
write_to_log = 'yes' #if yes, it prints the output in log.txt instead printing on screen
logfile = 'log.txt'

#log part 1
if write_to_log == 'yes':
	old_stdout = sys.stdout
	logfile = open(logfile,'w')
	sys.stdout = logfile
else:
	pass

# body
check_python()
format_sequences(infile)
while sorted_list != []:
	find_motifs(infile, motif_len, repetition)
	motif_len += 1

print('execution time :' + str(time.time() - start_time) + ' seconds\n')

#log part 2
if write_to_log == 'yes':
	sys.stdout = old_stdout #log END
	logfile.close() #close log_file
	sys.exit('program ran succesfully and its output has been written in log.txt')
else:
	pass
	
#exit
sys.exit('program ran succesfully')