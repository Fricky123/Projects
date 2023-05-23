todo_list = []
#-------------------------------------------------------------
def options():
    
    display_todo_list()
    
    print('1. Insert new todo')
    print('2. Delete todo')
    
    x = input("Option: ")
    
    if x == '1':
        insert_todo()
        
    elif x == '2':
        delete_todo()
        
    else:
        input('[error]')
        options()

def insert_todo():
    todo = input('Enter: ')
    
    todo_list.append(f'{len(todo_list) + 1}. {todo}')
    
    options()
    
def delete_todo():
    try:
        delete = int(input('Enter number: '))
        
        todo_list.pop(delete-1)
        
    except ValueError:
        input('[error]')
        options()
        
    except IndexError:
        input('[error: todo number does not exist]')
    
    options()
    
def display_todo_list():
    print("------------------------")
    print("My To Do List:\n")
    
    for x in todo_list:
        print(x)
        
    separator()

#-------------------------------------------------------------
def separator():
    print('#-------------------------------------------------------------')

#-------------------------------------------------------------
options()
        
    