import sqlite3
import subprocess as sp



def create_table():
	conn = sqlite3.connect('db')

	cursor = conn.cursor()

	query = '''
	    CREATE TABLE IF NOT EXISTS todo(
	    	id INTEGER PRIMARY KEY, 
	    	title TEXT, 
	    	description TEXT,
	        status INTEGER
	    )
	'''

	cursor.execute(query)

	conn.commit()
	conn.close()



def add_student(title,description,status):
	conn = sqlite3.connect('db')

	cursor = conn.cursor()

	query = '''
	    INSERT INTO todo( title,description,status)
	    	        VALUES ( ?,?,? )
	'''

	cursor.execute(query,(title,description,status))

	conn.commit()
	conn.close()



def get_students():
	conn = sqlite3.connect('db')

	cursor = conn.cursor()

	query = '''
	    SELECT id,title,description
	    FROM todo
	'''

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

def get_student_by_id(id):
	conn = sqlite3.connect('db')
	cursor = conn.cursor()
	query = '''
		select title,description,status
		from todo
		where id = {}'''.format(id)
	cursor.execute(query)
	all_rows = cursor.fetchone()

	conn.commit()
	conn.close()

	return all_rows


def get_student_by_roll(title):
	conn = sqlite3.connect('db')

	cursor = conn.cursor()

	query = '''
	    SELECT title,description,status
	    FROM todo
	    WHERE status = {}
	''' .format(title)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

def update_student(title,description,status,id):
	conn = sqlite3.connect('db')

	cursor = conn.cursor()
	if title == "" and description != "":
		query = '''
		    UPDATE todo
		    SET description = '{}', status = {}
		    WHERE id = {}
		'''.format(description,status, id)
	elif title == "" and description == "" :
		query = '''
		    UPDATE todo
		    SET  status = {}
		    WHERE id = {}
		'''.format(status, id)
	elif title != "" and description == "":
		query = '''
		    UPDATE todo
		    SET title = '{}', status = {}
		    WHERE id = {}
		'''.format(title,status, id)
	elif title != "" and description != "":
		query = '''
		    UPDATE todo
		    SET title = '{}', description = '{}', status = {}
		    WHERE id = {}
		'''.format(title,description,status, id)

	cursor.execute(query)

	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()
	print (all_rows)


def show_data_by_status(id_):
	students = get_student_by_roll(id_)
	if not students:
		print("No data found at status",id_)
	else:
		cursor.execute(query,(title,description,status))

		conn.commit()
		conn.close()


def delete_student(id):
	conn = sqlite3.connect('db')

	cursor = conn.cursor()

	query = '''
	    DELETE
	    FROM todo
	    WHERE id = {}
	''' .format(id)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows



create_table()



"""
main code
"""



def add_data(title,description,status):
	add_student(title,description,status)
def get_data():
	return get_students()

def show_data():
	students = get_data()
	head = ["id","Title","Description"]
	row_format ="|{:>5}" + ("|{:>30}" * (len(head) - 1))
	print(row_format.format(*head))
	for row in students:
		print("-"*120)
		print(row_format.format(*row))

def show_data_by_status(id_):
	students = get_student_by_roll(id_)
	if not students:
		print("No data found at status",id_)
	else:
		print (students)

def show_data_by_id(id__):
	students = get_student_by_id(id__)
	if not students:
		print("No data fount at status", id__)
	else:
		print(students)
def show_data_by_status(id_):
	students = get_student_by_roll(id_)
	if not students:
		print("No data found at status",id_)
	else:
		print (students)

def manage():
	sp.call('clear',shell=True)
	sel = input("1.Add Note\n2.Show Notes\n3.Get By Status\n4.Update\n5.Delete\n6.Exit\n\n")

	
	if sel=='1':
		sp.call('clear',shell=True)
		id_ = str(input('Title: '))
		name = str(input('Description: '))
		phone = str(input('Status (0-1): '))
		add_data(id_,name,phone)
	elif sel=='2':
		sp.call('clear',shell=True)
		show_data()
		input("\n\npress enter to back:")
	elif sel=='3':
		sp.call('clear',shell=True)
		id__ = int(input('Enter Status (0-1): '))
		show_data_by_status(id__)
		input("\n\npress enter to back:")
	elif sel=='4':
		sp.call('clear',shell=True)
		id__ = int(input('Enter Id: '))
		show_data_by_id(id__)
		print()
		title = str(input('Title: '))
		descrip = str(input('Description: '))
		status = int(input('Status: '))
		update_student(title,descrip,status,id__)
		input("\n\nYour data has been updated \npress enter to back:")
	elif sel=='5':
		sp.call('clear',shell=True)
		id__ = int(input('Enter Id: '))
		show_data_by_id(id__)
		delete_student(id__)
		input("\n\nYour data has been deleted \npress enter to back:")
	else:
		return 0;
	return 1;

while(manage()):
	pass
