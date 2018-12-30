import csv
import copy
import io


FILENAME = "train_data.tsv"
DICTIONARY = "portuguese_words.txt"

class File_manager:

	def __init__(self):
		return

	def get_instances_of_file(self):
		instances = []
		with open(FILENAME) as tsvfile:
			tsvreader = csv.reader(tsvfile, delimiter="\t")
			for instance in tsvreader:
				instances += [instance]
		return instances[1:]
	
	def read_dictionary(self):
		with io.open(DICTIONARY, mode="r", encoding="utf-8") as txtfile:
			txtread = txtfile.read()
		return ' '.join(txtread.splitlines())

