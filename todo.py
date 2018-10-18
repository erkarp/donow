#! python3
# todo.py - cl todos

import sys

PERMISSION = 'r'

PERMISSIONS = {
	'add': 'w',
	'del': 'w',
	'edit': 'w',
	'move': 'w',
	'view': 'r', 
	'raw': 'r',
	'clear': 'w'
} 

arg = 'view' if len(sys.argv) == 1 else sys.argv[1]

file = open('todo.txt', 'r')
todos = file.read().strip().split('\n')
file.close()

try: 
	PERMISSION = PERMISSIONS[arg]

	if PERMISSION == 'w':
		file = open('todo.txt', 'w')

		def save_todos(todos):
			file.write('\n'.join(todos))
			
		def get_arg_items():
			if len(sys.argv) > 2:
				return sys.argv[2:]
				
		def get_todo(todo):
			try:
				return todos[int(todo) - 1]
				
			except:
				if todo in todos:
					return todo
					
				else: 
					print('Invalid argument\n')
		
except: 
	print('Invalid argument')

		


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
			if (get_todo(todo)):
				todos.remove(get_todo(todo))

	else: 
		print('No todos selected.\n')


elif arg == 'edit':
	arg_todos = get_arg_items()
	success = False

	if arg_todos and 0 < len(arg_todos) < 3:
		old = get_todo(arg_todos[0])

		if old:
			if len(arg_todos) == 2:
				new = arg_todos[1].strip()
			else:
				new = input('edit item: ').strip()

		if new :
			index = todos.index(old)
			todos[index] = new
			success = True
		
	if not success:
		print('Invalid argument\n')


elif arg == 'move':
	arg_todos = get_arg_items()
	success = False

	if arg_todos and len(arg_todos) == 2:
		todo = get_todo(arg_todos[0])
		
		if (todo):
			success = True

			try: 
				old_index = todos.index(todo)
				new_index = int(arg_todos[1]) -1

				del todos[old_index]
				todos.insert(new_index, todo)
			
			except:
				print('Invalid new index\n')

	if not success:
		print('Invalid argument\n')

	
elif arg == 'clear':
	if (input('Delete all todos? (y/n)\n') == 'y'):
		todos = []
		
	
elif arg == 'view':
	print_todos(todos)
	
	
elif arg == 'raw':
	print(repr(todos))
	

if PERMISSION == 'w':
	save_todos(todos)
	print_todos(todos)
	file.close()
