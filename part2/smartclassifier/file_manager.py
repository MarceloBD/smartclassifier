import csv
import copy

FILENAME = "train_data.tsv"

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

