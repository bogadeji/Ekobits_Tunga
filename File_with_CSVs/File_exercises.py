# Part 1 - Text files
# Using only first names, and without unique ids


def add_student(first_name):
	with open('students.txt', 'a') as file:
		file.write(f'\n {first_name}')

		file.close()

def find_student(first_name):
    with open('students.txt', 'r') as file:
        for f in file:
            if f == first_name:
                print(f)

import re
def update_student(first_name, new_name):
	with open('students.txt', 'r+') as file:
		text = file.read()
		text = re.sub(first_name, new_name, text)
		file.seek(0)
		file.write(text)
		file.close()

def remove_student(first_name):
	with open('students.txt', 'r+') as file:
		text = file.read()
		text = re.sub(first_name, '', text)
		file.seek(0)
		file.write(text)
		file.close()

# Using unique ids

# random id using uuid1() 

import uuid 

def add_student(first_name):
	with open('students.txt', 'a') as file:
		student_id = uuid.uuid1()
		file.write(f'\n {first_name}|{student_id}')
		file.close()

def find_student(student_id):
    with open('students.txt', 'r') as csvfile:
    	reader = csv.reader(csvfile, delimiter='|')
    	for row in reader:
    		if student_id == row[-1]:
    			return (f'Record of student with id {student_id} exists')
    		else:
    			return (f'Record of student with id {student_id} does not exist')


# # Part 2 - CSV

def print_names():
	with open.('users.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile, delimiter='|')
		rows = list(reader)
		for row in rows:
			print(row)
		file.close()

def add_names(first_name, last_name):
	with open.('users.csv', 'a') as csvfile:
		data = [ 'first_name', 'last_name' ]
		data_writer = csv.DictWriter(csvfile, fieldnames=data)
		data_writer.writerow({'first_name': first_name: 'last_name': last_name})
		file.close(-)
