from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

import numpy as np

class Naive:

	def __init__(self):
		return

	def naive_bayes(self, instances):
		count_vect = CountVectorizer()
		x = [instance[1] for instance in instances]
		X_train_counts = count_vect.fit_transform(x)

		tfidf_transformer = TfidfTransformer()
		X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
		
		mnb = MultinomialNB()
		y =  [((instance[2])) for instance in instances]
        
		y_pred = mnb.fit(X_train_tfidf, y)

		docs_new = ['samsung celular', 'capa samsung', 'cororido azul boneca', 'apple']
		#docs_new = x
		
		X_new_counts = count_vect.transform(docs_new)
		X_new_tfidf = tfidf_transformer.transform(X_new_counts)

		predicted = y_pred.predict(X_new_tfidf)

		for doc, category in zip(docs_new, predicted):
			print('%r => %s' % (doc, category))
		#for category_index in range(len(predicted)):
		#	instances[category_index][2] = predicted[category_index]

		#with open("results.tsv", "w") as record_file:
		#	record_file.write("ID	TITLE	CATEGORY\n")
		#	for instance in instances:
		#		record_file.write(str(instance[0])+"	"+str(instance[1])+"	"+ str(instance[2])+"\n")
