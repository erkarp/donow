#! python3
# todo.py - cl todos

import sys

arg = 'view'
if len(sys.argv) > 1:
	arg = sys.argv[1]

if arg == 'add':
	file = open('todo.txt','a')
	new_todos = []

	while True:
		print('item todo:')
		todo = input()
		
		if todo == '':
			break
			
		new_todos.append('* ' + todo)
		
	file.write('\n'.join(new_todos))
	
	
elif arg == 'clear':
	if (input('Delete all todos? (y/n)\n') == 'y'):
		file = open('todo.txt','w')
		file.write('')
		
	
else: 
	file = open('todo.txt','r')
	todos = file.read()
	
	if arg == 'view':
		print(todos)
		
	elif arg == 'raw':
		print(repr(todos))
	

file.close()
