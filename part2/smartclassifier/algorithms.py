import numpy as np
import copy as cp

class Algorithms():
	
	def __init__(self):
		return
	
	def bag_of_words(self, words):
		bow = {'total_bow':len(words)}
		for word in words:
			bow[word] = bow.get(word, 0) + 1
		for word in bow:
			if(word == 'total_bow'):
				continue
			bow[word] /= bow['total_bow']
		return bow
	
	
	
	def laplace_smooth(self, word, bow, number_words):
		return bow.get(word, 1/(bow['total_bow']+number_words))
	
	def get_class_probability(self, words, bow):
		prob = 0
		words_dic ={}
		for word in words:
			words_dic[word] = 1
		new_words = {}
		for word in words_dic:
			if(not bow.get(word, 0)):
				new_words[word] = 1
		bow['total_bow'] += sum(new_words.values())	
		for word in words_dic:
			prob += np.log(self.laplace_smooth(word, bow, sum(new_words.values())+len(bow)))

		return np.abs(prob)
	
	def is_similar(self, bigger, smaller):
		bow = self.bag_of_words(bigger)
		for word in bow:
			if(bow[word] == 1/bow['total_bow']):
				print(bow[word])
				del bow[word]
				break
		bigger_min = cp.copy(bigger)
		for w_i in range(len(bigger_min)):
			if(word == bigger_min[w_i]):
				del bigger_min[w_i]
				break
		print(bow, bigger_min, bow['total_bow'])
		min_prob = self.get_class_probability(bigger_min, bow)
		prob = self.get_class_probability(smaller, bow)
		
		print(min_prob, prob)

			