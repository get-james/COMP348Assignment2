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
		return "Customer Removed"
	else: return "customer not found"


def update_field(name, field, update):#prolly won't work come back to it
	if(find_customer(name) == "customer not found"):
		return "customer not found"
	else:
		database[name][field] = update
		return "customer updated"

def add_customer(sent_list):
	if(find_customer(sent_list[1]) != "customer not found"):
		return "customer already exists"
	else:
		database[sent_list[1]] = sent_list[1:]
		return "success"

def send_report():
	return database

def data_reader(sent_list):#0 is choice 1 is name 2 is age 3 is address 4 is phone number
	choice = sent_list[0]
	if(choice == 1):
		return find_customer(sent_list[1])
	if(choice == 2):
		return add_customer(sent_list)
	if(choice == 3):
		return delete_customer(sent_list[1])
	if(choice == 4):
		return update_field(sent_list[1], 1, sent_list[2])
	if(choice == 5):
		return update_field(sent_list[1], 2, sent_list[2])
	if(choice == 6):
		return update_field(sent_list[1], 3, sent_list[2])
	if(choice == 7):
		return send_report()
	
