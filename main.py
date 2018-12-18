
from preprocessing import Preprocessing

if __name__ == "__main__":

	prepross = Preprocessing()

	instances = prepross.get_instances_of_file()
	prepross.pre_classfiy(instances)