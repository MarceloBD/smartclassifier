from file_manager import File_manager 
from naive import Naive

TRAIN_FILENAME = "train_data.tsv"
TEST_FILENAME = "data_estag_ds.tsv"


if __name__ == '__main__':
	filemng = File_manager()
	train_instances = filemng.get_instances_of_file(TRAIN_FILENAME)
	test_instances = filemng.get_instances_of_file(TEST_FILENAME)
	
	nv = Naive()
    
	dic = filemng.read_dictionary()
	
	nv.naive_bayes(train_instances, dic, test_instances)
    
