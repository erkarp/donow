#! python3
# todo.py - cl todos

import sys

PERMISSION = {
	'add': 'w',
	'del': 'w',
	'raw': 'r',
	'view': 'r', 
	'clear': 'w'
} 

arg = 'view' if len(sys.argv) == 1 else sys.argv[1]

file = open('todo.txt', 'r')
todos = file.read().strip().split('\n')
file.close()

try:
	if PERMISSION[arg] == 'w':
		file = open('todo.txt', 'w')
		
		def save_todos(todos):
			file.write('\n'.join(todos))
except: 
	print('Invalid argument')
	sys.exit()

		


def print_todos(list):
	count = 1
	for item in list:
		if item.isalnum():
			print(str(count) + '. ' + item)
			count += 1


		
if arg == 'add':
	if len(sys.argv) > 2:
		for i in range(2, len(sys.argv)):
			todos.append(sys.argv[i])
			
	else:
		while True:
			todo = input('item: ').strip()
				
			if todo == '':
				break
					
			todos.append(todo)
				
	save_todos(todos)
	print_todos(todos)
	

elif arg == 'del':
	if len(sys.argv) > 2:
		for i in range(2, len(sys.argv)):
			try:
				input = int(sys.argv[i])
				del todos[input - 1]
				save_todos(todos)
				print_todos(todos)
				
			except:
				print('NaN')

	else: 
		print('No todos selected.')

	
elif arg == 'clear':
	if (input('Delete all todos? (y/n)\n') == 'y'):
		file.write('')
		
	
elif arg == 'view':
	print_todos(todos)
	
	
elif arg == 'raw':
	print(repr(todos))
	

if PERMISSION[arg] == 'w':
	file.close()
