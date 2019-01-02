from file_manager import File_manager


TEST_FILENAME = "results.tsv"
MAX_RAM_DIGITS = 10
COLORS = ['azul topázio', 'azul', 'verde', 'preto', 'branco', 'prata', 'platinum', 'indigo', 'dourado','ouro rosé',
		  'ouro', 'cinza', 'índigo', 'rose gold', 'rose', 'titanium', 'ametista', 'rosa', 'gold', 
		  'vermelho', 'ultravioleta', 'black', 'titânio', 'red', 'violeta']
MAX_SIZE_DIGITS = 10
STOP_WORDS = ["com", "tela", "android", "-"]
INSIDE_STOP_WORDS = [",", "."]
SIDE_STOP_WORDS = ['+']

def is_valid_ram(ram):
	if(len(ram) != 0 and (ram[-1]=='b' and ram[-2]=='g')):
		for c_i in range(0, len(ram)-2):
			if(not ram[c_i].isdigit()):
				return False
		return True
	elif(len(ram) != 0 and ram[-1] =='g'):
		for c_i in range(0, len(ram)-1):
			if(not ram[c_i].isdigit()):
				return False
		return True
	return False



def is_word_in_string(string):
	for word in STOP_WORDS+COLORS:
		if(' '+ word+' ' in string.lower() or ' '+ word+',' in string.lower()):
			for i in range(len(string)-2, 0, -1):
				if( string[i] == " "):
					break
				else:
					string = string[:i]
			return [True, string]
	
	for word in INSIDE_STOP_WORDS:
		if(word in string.lower()):
			for i in range(len(string)-2, 0, -1):
				if( string[i] == " "):
					break
				else:
					string = string[:i]
			return [True, string]
	for word in SIDE_STOP_WORDS:
		if(' '+word in string.lower()):
			for i in range(len(string)-2, 0, -1):
				if( string[i] == " "):
					break
				else:
					string = string[:i]
			return [True, string]
		
	ram = ''
	for c_i in range(len(string)-2, 0, -1):
		if(string[c_i] == " "):
			break
		else:
			ram += string[c_i]
	if(is_valid_ram(ram[::-1].lower())):
		for i in range(len(string)-2, 0, -1):
			if( string[i] == " "):
				break
			else:
				string = string[:i]
		return [True, string]
	return [False, string]
	
def get_data_from_title(smartphone):
	title = smartphone[1]
	i_title = 0
	specs = []
	name = ""
	for i in range(len(title)):
		name += title[i].lower()
		if(title[i] == " " or title[i]==','):
			[ended, name] = is_word_in_string(name)
			if(ended):
				break
	
	specs += [name]
	
	
	ram = ""
	i_ram = 0
	for i in range(i_title, len(title)):
		if(i+2 < len(title) and title[i].lower() == 'r' and title[i+1].lower() == 'a' and title[i+2].lower()== 'm'):
			i_ram = i+4 
			for not_numbers in range(i-2, i-MAX_RAM_DIGITS, -1):
				if(title[not_numbers].isdigit()):
					break
				elif(title[not_numbers] == " "):
					i = not_numbers+1
					break
			for j in range(i-1, i-MAX_RAM_DIGITS, -1):
#				print(title)
				if(title[j-1] != " "):
					ram += title[j-1]
				else:
					break
			break
	ram = ram[::-1].lower()
	
	if(not is_valid_ram(ram)):
		ram = ''
		for not_numbers in range(i_ram, i_ram+MAX_RAM_DIGITS):
			if(not_numbers >= len(title) or title[not_numbers].isdigit()):
				break
			elif(title[not_numbers] == " "):
				i_ram = not_numbers+1
				break
		for j in range(i_ram, i_ram+MAX_RAM_DIGITS):
			if(j < len(title) and title[j] != " "):
				ram += title[j]
			else:
				break
	ram = ram.lower()
	if(not is_valid_ram(ram)):
		ram = ''
	if(len(ram) and ram[-1] == 'g'):
		ram += 'b'
	specs += [ram]
		
	col = ""
	for color in COLORS:
		if(color in title.lower()):
			col = color 
			break
	specs += [col]
		
	
	size = ""
	for i in range(len(title)):

		if(title[i] == "'" or title[i] == '"' or title[i] == '”'):
			for j in range(i-1, i-MAX_SIZE_DIGITS, -1):
				if(title[j] == " "):
					break
				size += title[j]
			size = size[::-1]
			break
		if(title[i] == '.' or title[i] == ','):
			point = False
			if(not title[i-1].isdigit() or not title[i+1].isdigit()):
				continue
			while(title[i] != " "):
				i -= 1
			
			for j in range(i+1, i+MAX_SIZE_DIGITS):
				if(j >= len(title)):
					break
				if(title[j] == " "  or title[j] == '”' or title[j] == "'" or title[j] == '"'):
					break
				elif(title[j] == '.' or title[j] == ',' or not title[j].isdigit()):
					if(point):
						break
					else:
						if(title[j] != '.' and title[j] != ',' and not title[j].isdigit()):
							size = ''
							break
						else:
							point = True
				size += title[j]
			break
	#print(title)
	if(len(size) > 5):
		size = ''
	for c_i in range(len(size)):
		if(size[c_i] == '.'):
			size = size[:c_i]+','+size[c_i+1:]
			break
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

#[print(smartphone) for smartphone in only_smartphones]

with open("extracted_info.tsv", "w", encoding = "utf-8") as record_file:
			record_file.write("ID	TITLE	NAME	RAM	COLOR	SCREEN SIZE\n")
			for instance in only_smartphones:
				record_file.write(str(instance[0])+"	"+str(instance[1])+"	"+ str(instance[3][0])+"	"+ str(instance[3][1])+
					  "	"+ str(instance[3][2])+"	"+ str(instance[3][3])+"\n")