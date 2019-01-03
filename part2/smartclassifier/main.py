from file_manager import File_manager 
from naive import Naive
from datamuse import Datamuse
import asyncio

TRAIN_FILENAME = "train_data.tsv"
TEST_FILENAME = "data_estag_ds.tsv"


if __name__ == '__main__':
	
	filemng = File_manager()
	train_instances = filemng.get_instances_of_file(TRAIN_FILENAME)
	test_instances = filemng.get_instances_of_file(TEST_FILENAME)
	
	nv = Naive()    
	dic = filemng.read_dictionary()		
	dtmuse = Datamuse()	

	loop = asyncio.get_event_loop()  
	category_synonymous = loop.run_until_complete(dtmuse.get_synonymous('smartphone'))  
	loop.close() 
	category_synonymous = eval(category_synonymous)

	nv.naive_bayes(train_instances, dic, test_instances, category_synonymous)   