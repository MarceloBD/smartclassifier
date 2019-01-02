from file_manager import File_manager
from algorithms import Algorithms

SPECS_FILENAME = "extracted_info.tsv"













filemng = File_manager()
test_instances = filemng.get_instances_of_file(SPECS_FILENAME)

alg = Algorithms()

#bow = alg.bag_of_words('casa com wifi e celular'.split())
#print(alg.get_class_probability('casa com wifi e'.split(), bow))
alg.is_similar('casa com wifi 2'.split(), 'casa com wifi'.split())