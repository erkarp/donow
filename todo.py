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
todos = file.read().split('\n')
file.close()

if PERMISSION[arg] == 'w':
	file = open('todo.txt', 'w')
	
	


def print_items(list):
	for item in list:
		print(item)

		
if arg == 'add':
	count = len(todos)
	
	while True:
		print('item todo:')
		todo = input()
			
		if todo == '':
			break
				
		todos.append(str(count) + '. ' + todo)
		count += count
			
	file.write('\n'.join(todos))

	
elif arg == 'clear':
	if (input('Delete all todos? (y/n)\n') == 'y'):
		file.write('')
		
	
elif arg == 'view':
	print_items(todos)
	
	
elif arg == 'raw':
	print(repr(todos))
	

if PERMISSION[arg] == 'w':
	file.close()
