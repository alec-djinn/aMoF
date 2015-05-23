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
		print('*****************************')
		with open(out_file, 'w') as out_file:
			out_file.write(merged_sequences)
			print('>>>merged sequence' + '\n' + merged_sequences)
#****************END*OF*FUNCTION****************

merge_sequences('Phage Display - PhDC7C - Acid Elution 3 - Plate 2 - Sequencing results.txt', 'merged_sequences.txt')