def file_reader():
	f = open("data.txt", "r")
	global database
	database = dict()
	for x in f:
		a = x.split("|")
		
		for i in range(len(a)):#cleaning up 
			a[i] = a[i].strip()
			a[i] = a[i].strip('\n')
		
		if(a[0]!= ""):
			database[a[0]] = a #setting name as the key in the dictionary
			
			

	for x in database:
		print(database[x])




def find_customer(name):
	return database.get(name, "customer not found")

def delete_customer(name):
	if(find_customer(name)!= "customer not found"):
		database.pop(name)
	else: return "customer not found"


def update_field(name, field, update):#prolly won't work come back to it
	if(find_customer(name) == "customer not found"):
		return "customer not found"
	else:
		database[name][field] = update

def add_customer(name, fields):
	if(find_customer(name) != "customer not found"):
		return "customer already exists"
	else:
		entry = fields.split("|")
		database[entry[0]] = entry
		return "success"

def send_report():
	return database

def data_reader(sent_list):
	choice = sent_list[0]
	if(choice == 1):
		return find_customer(sent_list[1])
	if(choice == 2):
		add_customer(sent_list[1], sent_list[1:-1])
