import csv
import copy
import io


DICTIONARY = "portuguese_words.txt"

class File_manager:

	def __init__(self):
		return

	def get_instances_of_file(self, filename):
		instances = []
		with open(filename, encoding='utf-8', errors='ignore') as tsvfile:
			tsvreader = csv.reader(tsvfile, delimiter="\t")
			for instance in tsvreader:
				instances += [instance]
		return instances[1:]
	
	def read_dictionary(self):
		with io.open(DICTIONARY, mode="r", encoding="utf-8") as txtfile:
			txtread = txtfile.read()
		return ' '.join(txtread.splitlines())

