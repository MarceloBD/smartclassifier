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
			synonymous += [sym["word"]]
		return synonymous
	
	def naive_bayes(self, train_instances, dic, test_instances, synonymous_response):
		
		dic = ' '.join([word for word in dic.split() if len(word) > 4])
		synonymous = self.clean_synonymous_response(synonymous_response)
		synonymous = ' '.join(synonymous)
		
		train_instances = []	
		dic_list = dic.split()
		syn_list = synonymous.split()
		syn_list += ['smartphone', 'celular', 'apple']
		
		for word in dic_list:
			train_instances += [['dictionary from github', word, 'nao-smartphone']]

		for i in range(len(dic_list)):
			train_instances += [['category synonymous', syn_list[i%len(syn_list)], 'smartphone']]
		
		
		count_vect = CountVectorizer()
		x = [instance[1] for instance in train_instances]
		X_train_counts = count_vect.fit_transform(x)

		tfidf_transformer = TfidfTransformer(use_idf = False)
		X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
		
		mnb = MultinomialNB()
		y =  [((instance[2])) for instance in train_instances]
        
		y_pred = mnb.fit(X_train_tfidf, y)

		x = [instance[1].split()[0].lower() for instance in test_instances]
		docs_new = x
		
		X_new_counts = count_vect.transform(docs_new)
		X_new_tfidf = tfidf_transformer.transform(X_new_counts)

		predicted = y_pred.predict(X_new_tfidf)

		for category_index in range(len(predicted)):
			test_instances[category_index] += [predicted[category_index]]

		with open("results.tsv", "w", encoding = "utf-8") as record_file:
			record_file.write("ID	TITLE	CATEGORY\n")
			for instance in test_instances:
				record_file.write(str(instance[0])+"	"+str(instance[1])+"	"+ str(instance[2])+"\n")
