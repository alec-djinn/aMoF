import unittest
from amof import *

class SequenceParsersTests(unittest.TestCase):
	
	def test_is_id(self):
		'''Test if it recognizes a string containing a valid sequence id.'''
		self.assertTrue(is_id('>seq1'))
		self.assertTrue(is_id('seq1'))
		self.assertFalse(is_id('acgtaagtcggat'))

	def test_auto_parse(self):
		'''Test if a string containing one or multiple sequences is parsed correctly.'''
		self.assertEqual(auto_parse('>seq1\nAAAAGGGG'),
						 OrderedDict([('>seq1', 'AAAAGGGG')]))
		
		self.assertEqual(auto_parse('>seq1\nAAAA\n>seq2\nGGGG'),
						 OrderedDict([('>seq1', 'AAAA'), ('>seq2', 'GGGG')]))

		self.assertEqual(auto_parse('>seq1\nAAAA\nseq2\nGGGG'),
						 OrderedDict([('>seq1', 'AAAA'), ('>seq2', 'GGGG')]))

		self.assertEqual(auto_parse('>seq1\nAA\n\n\nAA\nseq2\nGG\nGG\n'),
						 OrderedDict([('>seq1', 'AAAA'), ('>seq2', 'GGGG')]))



class MotifFindersTests(unittest.TestCase):
	
	def test_simple_finder(self):
		'''Test the very basic motif finder algorithm'''
		self.assertEqual(simple_finder({'>seq1':'AAAArepeatGGGGrepeatFFFFrepeat'},len('repeat'),2),
						 OrderedDict([('repeat', 3)]))

		self.assertEqual(simple_finder({'>seq1':'AAAArepeatGGGGrepeatFFFFrepeat'},len('repeat'),3),
						 OrderedDict([('repeat', 3)]))

		self.assertEqual(simple_finder({'>seq1':'AAAArepeatGGGGrepeatFFFFrepeat'},len('repeat'),4),
						 OrderedDict())

		self.assertEqual(simple_finder({'>seq1':'AAAArepeatGGGGrepeatFFFFrepeat',
			                            '>seq2':'BBBBrepeatXXXrepeatKKrepeat'},len('repeat'),2),
						 OrderedDict([('repeat', 6)]))

		self.assertEqual(simple_finder({'>seq1':'AAAAYrepeatGGGGrepeatFFFFrepeat',
			                            '>seq2':'BBBBrepeatXXXYrepeatKKrepeat'},len('repeat'),2),
						 OrderedDict([('repeat', 6),('Yrepea',2)]))





if __name__ == '__main__':
	unittest.main()