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

		tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
		X_train_tf = tf_transformer.transform(X_train_counts)

		tfidf_transformer = TfidfTransformer()
		#X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
		
		mnb = MultinomialNB()
		#instances = np.array(instances)
		#x = [instance[1] for instance in instances]
		#print(x)
		y =  [((instance[2])) for instance in instances]

		y_pred = mnb.fit(X_train_tf, y)
		
		docs_new = ['smartphone', 'capinha', 'boneca azul verde s2 colorida', 'apple']
		
		X_new_counts = count_vect.transform(docs_new)
		tf_transformer = TfidfTransformer(use_idf=False).fit(X_new_counts)
		X_new_tfidf = tf_transformer.transform(X_new_counts)

		predicted = y_pred.predict(X_new_tfidf)

		for doc, category in zip(docs_new, predicted):
			print('%r => %s' % (doc,category))
		#print("Number of mislabeled points out of a total %d points : %d" 
		#	% (instances[:,1].shape[0],(instances[:,2] != y_pred).sum()))