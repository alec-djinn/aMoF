from collections import OrderedDict
from operator import itemgetter

def is_id(line):
	'''Determine if a line of text contains a sequence id_.
	Return True of False.
	'''
	specials = ['>','<',':','.','_','-','[',']''{','}',
	            '0','1','2','3','4','5','6','7','8','9']
	for s in specials:
		if s in line[:50]:
			return True
	return False


def auto_parse(input_sequence):
	'''Parse a text looking for biological sequence/s and relative id_/s.
	Return an OrderedDict having id_:sequence as key:value in a FASTA format.
	If one ore more id are missing a random id with the 'amof_' suffix will be generated instead.
	'''
	comments = ['/','\\','#']
	blanks   = ['',' ','\t','\n']
	
	id_  = None
	sequence    = None
	input_error = False
	duplicate 	= 0

	d = OrderedDict()

	lines = input_sequence.split('\n')
	for line in lines:
		if len(line):
			if line[0] not in (comments+blanks): #skip comments and blanks
				if is_id(line):
					id_ = line.strip()
					if not id_.startswith('>'):
						id_ = '>'+id_
					if id_ not in d:
						d.update({id_:''})
					else:
						id_ += '_'+duplicate
						duplicate += 1

				else:
					sequence = line.strip().replace(' ','').replace('\t','')
					d[id_] += sequence
	return d


def simple_finder(sequence_dict, motif_length, min_repetition):
	'''(dict, int, int) -> OrderedDict
	Find all the motifs long 'motif_length' and repeated at least 'min_repetition' times.
	Return an OrderedDict having motif:repetition as key:value sorted by value. 
	'''
	motif_dict = {}
	for id_, sequence in sequence_dict.items():
		#populate a dictionary of motifs (motif_dict)
		for i in range(len(sequence) - motif_length +1):
			motif = sequence[i:i+motif_length]
			if motif not in motif_dict:
				motif_dict[motif] = 1
			else:
				motif_dict[motif] += 1

	#remove from motif_dict all the motifs repeated less than 'repetition' times
	keys_to_remove = [key for key, value in motif_dict.items() if value < min_repetition]
	for key in keys_to_remove:
		del motif_dict[key]
	
	#Return a sorted dictionary
	return OrderedDict(sorted(motif_dict.items(), key=itemgetter(1), reverse=True))


def mismatch_finder(sequence, motif_length, max_mismatch):
	'''Find the most frequent k-mers with mismatches in a string.
	Input: A sequence and a pair of integers: motif_length (≤ 12) and max_mismatch (≤ 3).
	Output: A lis containing all most frequent k-mers with up to d mismatches in string.

	Sample Input:	ACGTTGCATGTCGCATGATGCATGAGAGCT 4 1
	Sample Output:	GATG ATGC ATGT
	'''
 	
	#check passed variables
	if not motif_length <= 12 and motif_length >= 1:
		raise ValueError("motif_length must be between 0 and 12. {} was passed.".format(motif_length))
	if not max_mismatch <= 3 and max_mismatch >= 1:
		raise ValueError("max_mismatch must be between 0 and 3. {} was passed.".format(max_mismatch))

	
	#find unique k-mers in the sequence
	motif_dict = {}	 
	for i in range(len(sequence) - motif_length +1):
		motif = sequence[i:i+motif_length]
		if motif not in motif_dict:
			motif_dict[motif] = 1
		else:
			motif_dict[motif] += 1
	

	#make a list of motif
	motif_list = []
	for k in motif_dict:
		motif_list.append(k)
	

	#check where the motifs are [wrongly commented]
	temp = {}
	ylist = []
	for item in motif_list:
		motif = item
		results = []
		y = 0
		for n in range(len(sequence)-len(motif)+1):
			counter = 0
			sample = sequence[n:n+len(motif)]
			for i in range(len(sample)):
				if sample[i] == motif[i]:
					pass
				else:
					counter += 1
			if counter <= max_mismatch:
				results.append(n)
		
		temp[item] = []
		for value in results:
			temp[item].append(value)
			y += 1
		ylist.append(y)

	final_list = []
	for item in temp:
		if len(temp[item]) == max(ylist):
			final_list.append(item)

	return sorted(final_list)



