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
			
		def get_arg_items():
			if len(sys.argv) > 2:
				return sys.argv[2:]
		
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
	arg_todos = get_arg_items()
	
	if arg_todos:
		for todo in arg_todos:
			todos.append(todo)
			
	else:
		while True:
			todo = input('item: ').strip()
				
			if todo == '':
				break
					
			todos.append(todo)
	

elif arg == 'del':
	arg_todos = get_arg_items()
	
	if arg_todos:
		arg_todos.sort(reverse=True)
		
		for todo in arg_todos:
			try:
				del todos[int(todo) - 1]
				
			except: 
				try: 
					todos.remove(todo)
				
				except:
					print('Invalid argument\n')

	else: 
		print('No todos selected.')

	
elif arg == 'clear':
	if (input('Delete all todos? (y/n)\n') == 'y'):
		save_todos([])
		
	
elif arg == 'view':
	print_todos(todos)
	
	
elif arg == 'raw':
	print(repr(todos))
	

if PERMISSION[arg] == 'w':
	save_todos(todos)
	print_todos(todos)
	file.close()
