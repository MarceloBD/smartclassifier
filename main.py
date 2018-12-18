
from preprocessing import Preprocessing
from naive import Naive

if __name__ == "__main__":

	prepross = Preprocessing()

	instances = prepross.get_instances_of_file()
	preclassified_instances = prepross.pre_classfiy(instances)
	#prepross.bag_of_words(preclassified_instances)

	nv = Naive()
	nv.naive_bayes(preclassified_instances)