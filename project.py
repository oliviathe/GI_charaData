from os import system
import sys
from json import load, dump


# Input Check

def check_input(char):
	if char == "Q":
		sys.exit()
	elif char == "1":
		print_chara()
	elif char == "2":
		add_chara()
	elif char == "3":
		find_chara()
	elif char == "4":
		edit_chara()
	elif char == "5":
		delete_chara()

def verify_ans(char):
	char = char.upper()
	if char == "Y":
		return True
	else:
		return False


# System

def load_data():
	global chara_data
	with open(file_path, 'r') as document:
		chara_data = load(document)

def save_data():
	global chara_data
	with open(file_path, 'w') as document:
		dump(chara_data, document)

def create_slot_number():
	counter = len(chara_data)+1
	slot_number = str("slot%2d" % counter)
	return slot_number

def slot_number_from_name(chara):
	for slot_number in chara_data:
		if chara_data[slot_number]["name"] == chara:
			return slot_number

def print_data(slot_number = None, all_fields = False, element = True):
	if slot_number != None and all_fields == False:
		print(f"""
| Character Found |
- {chara_data[slot_number]["name"]} -
Role : {chara_data[slot_number]["role"]}
Element : {chara_data[slot_number]["element"]}
		""")
	elif all_fields == True:
		for slot_number in chara_data:
			name = chara_data[slot_number]["name"]
			role = chara_data[slot_number]["role"]
			element = chara_data[slot_number]["element"]
			print(f"Name : {name}\tRole : {role}\tElement : {element}")

def search_chara(chara):
	for slot_number in chara_data:
		if chara_data[slot_number]["name"] == chara:
			print_charaData(slot_number = slot_number)
			return True
		else:
			print("Character not found")
			return False

def view_menu():
	system("cls")
	menu = """
| Genshin Impact Party Manager |

[1] View Owned Characters
[2] Add Character
[3] Find Character
[4] Edit Character
[5] Delete Character
[I] About App
[Q] Quit
"""
	print(menu)

def view_chara():
	system("cls")
	print("| Owned Characters |")
	if len(chara_data) == 0:
		print("Character data is empty")
	else:
		print_data(all_fields = True)
	input("Press ENTER to go back to Menu")

def add_chara():
	system("cls")
	print("| Add Character |")
	if len(chara_data) >= 99:
		print("Stop whaling. Get a life.")
	else:
		name = input("Name : ").title()
		role = input("Role : ").title()
		element = input("Element : ").title()

		user_ans = input("Press Y to continue : ")

		if verify_ans(user_ans):
			slot_number = create_slot_number()
			print("Saving data . . .")
			chara_data[slot_number] = {
				"name" : name,
				"role" : role,
				"element" : element
				}
			save_data()
			print("Data saved!")
		else:
			print("Data saving is canceled")
	input("Press ENTER to go back to Menu")

def find_chara():
	system("cls")
	print("| Find Character |")
	if len(chara_data) == 0:
		print("Character data is empty")
	else:
		name = input("Character to find : ").title()
		result = search_chara(name)
	input("Press ENTER to go back to Menu")

def edit_name(chara):
	new_name = input("Edited name : ").title()
	response = input("Press Y to continue : ")
	if verify_ans(response):
		slot_number = slot_number_from_name(chara)
		chara_data[slot_number]["name"] == new_name
		save_data()
		print("Data edited!")
	else:
		print("Data saving is canceled")

def edit_role(chara):
	new_role = input("Edited role : ").title()
	response = input("Press Y to continue : ")
	if verify_ans(response):
		slot_number = slot_number_from_name(chara)
		chara_data[slot_number]["role"] == new_role
		save_data()
		print("Data edited!")
	else:
		print("Data saving is canceled")

def edit_element(chara):
	new_element = input("Edited element : ").title()
	response = input("Press Y to continue : ")
	if verify_ans(response):
		slot_number = slot_number_from_name(chara)
		chara_data[slot_number]["element"] == new_element
		save_data()
		print("Data edited!")
	else:
		print("Data saving is canceled")

def edit_chara():
	system("cls")
	print("| Edit Character |")
	name = input("Character to be edited : ")
	result = search_chara(name)
	if result:
		print(f"""
[1] Name
[2] Role
[3] Element
			""")
		response = input("Data to be edited : ")
		if response == "1":
			edit_name()
		elif response == "2":
			edit_role()
		elif response == "3":
			edit_element()
	input("Press ENTER to go back to Menu")

def delete_chara():
	print_header("| Delete Character |")
	name = input("Character to be deleted : ").title()
	result = search_chara(name)
	if result:
		response = input("Press Y to continue : ")
		if verify_ans(response):
			slot_number_from_name(name)
			del chara_data[slot_number]
			save_data()
			print("Data deleted")
		else:
			print("Data deleting is canceled")
	input("Press ENTER to go back to Menu")
			

# Main Program

file_path = 'project_storage.json'
chara_data = None
stop = False

load_data()

while not stop:
	view_menu()
	menu_userInput = input("Choice : ").upper()
	check_menu_input(menu_userInput)