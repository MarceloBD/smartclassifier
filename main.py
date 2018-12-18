
from preprocessing import Preprocessing

if __name__ == "__main__":

	prepross = Preprocessing()

	instances = prepross.get_instances_of_file()
	preclassified_instances = prepross.pre_classfiy(instances)
	prepross.bag_of_words(preclassified_instances)