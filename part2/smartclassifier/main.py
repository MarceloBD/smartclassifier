from file_manager import File_manager 
from naive import Naive

if __name__ == '__main__':

    filemng = File_manager()
    instances = filemng.get_instances_of_file()

    nv = Naive()
    nv.naive_bayes(instances)
