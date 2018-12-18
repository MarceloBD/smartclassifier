import csv
import copy

FILENAME = "data_estag_ds.tsv"
WORDS_FOR_PRECLASSIFIER = ["smartphone", "celular", "iphone", "samsung", "motorola"]
NOT_WORDS_FOR_PRECLASSIFIER = ["capa", "bumper", "tablet", "kit", "película", "repetidor", 
	"bracadeira", "cabo", "antena",  "suporte"]

class Preprocessing:

	def __init__(self):
		return

	def get_instances_of_file(self):
		instances = []
		with open(FILENAME) as tsvfile:
			tsvreader = csv.reader(tsvfile, delimiter="\t")
			for instance in tsvreader:
				instances += [instance]
		return instances


	def pre_classfiy(self, instances):
		for instance in instances:
			instance += ["nao-smartphone"]
			description = instance[1:][0].split()
			for word_index in range(len(description)):
				description[word_index] = description[word_index].lower()
				for defined_word in WORDS_FOR_PRECLASSIFIER:
					if(description[word_index] == defined_word):
						instance[2] = "smartphone"
						break
			for word_index in range(len(description)):
				for defined_word in NOT_WORDS_FOR_PRECLASSIFIER:
					if(description[word_index] == defined_word):
						instance[2] = "nao-smartphone"
						break
					#instance[1] = description
		return instances[1:]

	def bag_of_words(self, instances):
		bow ={"nao-smartphone":{}, "smartphone":{}}
		for instance in instances:
			for word in instance[1]:
				bow[instance[2]][word] = bow[instance[2]].get(word, 0) + 1 
		print(bow)

		return bow
