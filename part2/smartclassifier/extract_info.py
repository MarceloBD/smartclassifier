from file_manager import File_manager
import numpy as np

TEST_FILENAME = "results.tsv"
MAX_RAM_DIGITS = 10
COLORS = ['azul', 'verde', 'preto', 'branco', 'prata', 'platinum', 'indigo', 'dourado']
MAX_SIZE_DIGITS = 10

def get_data_from_title(smartphone):
	title = smartphone[1]
	i_title = 0
	specs = []
	name = ""
	for i in range(len(title)):
		if(title[i].isdigit() and i > 0 and title[i-1] == " "):
			for color in COLORS:
				 name = name.lower().replace(color, "")
			i_title = i 
			break
		name += title[i]
			
	
	specs += [name]
	
	
	ram = ""
	for i in range(i_title, len(title)):
		#print(title[i])
		if(i+2 < len(title) and title[i].lower() == 'r' and title[i+1].lower() == 'a' and title[i+2].lower()== 'm'):
			for not_numbers in range(i-2, i-MAX_RAM_DIGITS, -1):
				if(title[not_numbers].isdigit()):
					break
				elif(title[not_numbers] == " "):
					i = not_numbers
					break
			for j in range(i-1, i-MAX_RAM_DIGITS, -1):
				print(title)
				if(title[j-1] != " "):
					ram += title[j-1]
				else:
					break
			break
	specs += [ram[::-1]]
		
	col = ""
	for color in COLORS:
		if(color in title.lower()):
			col = color 
			break
	specs += [col]
		
	
	size = ""
	for i in range(len(title)):
		if(title[i] == "'" or title[i] == '"'):
			for j in range(i, i-MAX_SIZE_DIGITS, -1):
				if(title[j] == " "):
					break
				size += title[j]
			break
		if(title[i] == '.' or title[i] == ','):
			print('hereee', title[i])
			while(title[i] != " "):
				i -= 1
			
			for j in range(i+1, i+MAX_SIZE_DIGITS):
				if(j >= len(title)):
					break
				if(title[j] == " "):
					break
				size += title[j]
	specs += [size]
	smartphone += [specs]
	return smartphone


filemng = File_manager()
test_instances = filemng.get_instances_of_file(TEST_FILENAME)
only_smartphones = []
for obj in test_instances:
	if (obj[2] == 'smartphone'):
		only_smartphones += [obj]

for smartphone in only_smartphones:
	smartphone = get_data_from_title(smartphone)

[print(smartphone) for smartphone in only_smartphones]

with open("extracted_info.tsv", "w", encoding = "utf-8") as record_file:
			record_file.write("ID	TITLE	NAME	RAM	COLOR	SCREEN SIZE\n")
			for instance in only_smartphones:
				record_file.write(str(instance[0])+"	"+str(instance[1])+"	"+ str(instance[3][0])+"	"+ str(instance[3][1])+
					  "	"+ str(instance[3][2])+"	"+ str(instance[3][3])+"\n")