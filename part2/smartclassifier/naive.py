from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

import numpy as np

class Naive:

	def __init__(self):
		return


	def clean_synonymous_response(self, synonymous_response):
		synonymous = []
		for sym in synonymous_response:
			#print(sym)
			synonymous += [sym["word"]]
		return synonymous


	def transform_string_one_word_document(self, words, category, source):
		l = []
		for word in words.split():
			l += [[source, word, category]]
		return l
	
	def naive_bayes(self, train_instances, dic, test_instances, synonymous_response):
		
		synonymous = self.clean_synonymous_response(synonymous_response)
		synonymous = ' '.join(synonymous)
		
		sym_list = self.transform_string_one_word_document(synonymous, 'smartphone', 'category with datamuse')
		dic_list = self.transform_string_one_word_document(dic, 'nao-smartphone', 'dictionary from github')
		
		
		'''
		for l in sym_list:
			train_instances += [l]
		for l in sym_list:
			train_instances += [l]
		for l in dic_list:
			train_instances += [l]
		'''
		
		train_instances += [['dictionary from github', dic, 'nao-smartphone']]
		train_instances += [['dictionary from github', dic, 'nao-smartphone']]
		train_instances += [['dictionary from github', dic, 'nao-smartphone']]
		train_instances += [['dictionary from github', dic, 'nao-smartphone']]
		train_instances += [['dictionary from github', dic, 'nao-smartphone']]
		train_instances += [['dictionary from github', dic, 'nao-smartphone']]
		train_instances += [['dictionary from github', dic, 'nao-smartphone']]
		train_instances += [['dictionary from github', dic, 'nao-smartphone']]
		train_instances += [['category synonymous', synonymous, 'smartphone']]
		train_instances += [['category synonymous', synonymous, 'smartphone']]
		train_instances += [['category synonymous', synonymous, 'smartphone']]
		
		
		
		count_vect = CountVectorizer()
		x = [instance[1] for instance in train_instances]
		X_train_counts = count_vect.fit_transform(x)

		tfidf_transformer = TfidfTransformer()
		X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
		
		mnb = MultinomialNB()
		y =  [((instance[2])) for instance in train_instances]
        
		y_pred = mnb.fit(X_train_tfidf, y)

		#docs_new = ['samsung', 'capa smartphone', 'colorido azul boneca', 'apple']
		x = [instance[1] for instance in test_instances]
		docs_new = x
		
		X_new_counts = count_vect.transform(docs_new)
		X_new_tfidf = tfidf_transformer.transform(X_new_counts)

		predicted = y_pred.predict(X_new_tfidf)

		#for doc, category in zip(docs_new, predicted):
		#	print('%r => %s' % (doc, category))
		#if(test_instances[0][1][0:10] == 'Acessório' or test_instances[0][1][0:10] == 'Acessório '):
		#	print(test_instances[0][1][0:10])
		#print(test_instances[0][1][0:10])
		for category_index in range(len(predicted)):
			test_instances[category_index] += [predicted[category_index]]

		with open("results.tsv", "w", encoding = "utf-8") as record_file:
			record_file.write("ID	TITLE	CATEGORY\n")
			for instance in test_instances:
				record_file.write(str(instance[0])+"	"+str(instance[1])+"	"+ str(instance[2])+"\n")
