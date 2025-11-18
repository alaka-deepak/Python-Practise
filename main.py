while True:
    user_action=input("Type add,show,edit,complete or exit:")
    user_action=user_action.strip()

    if user_action.startswith('add'):
        todo=user_action[4:]

        with open('todos.txt','r') as file:
            todos=file.readlines()
        
        todos.append(todo)

        with open('todos.txt','w') as file:
            file.writelines(todos)
        
    elif user_action.startswith('show'):
        with open('todos.txt','r') as file:
            todos=file.readlines()
        

        for index,item in enumerate(todos):
            item=item.strip('\n')
            row=f"{index+1} - {item}"
            print(row)
        
    elif user_action.startswith('edit'):

        number=int(input("Number of the todo to edit"))
        number=number-1

        with open('todos.txt','r') as file:
            todos=file.readlines()

        new_todo=input("Enter new todo:")
        todos[number]=new_todo+'\n'

        with open('todos.txt','w') as file:
            file.writelines(todos)
    elif user_action.startswith('complete'):
        number=int(input("Number of the todo to edit"))
        with open('todos.txt','r') as file:
            todos=file.readlines()
        
        index=number-1
        todo_to_remove=todos[index].strip('\n')
        todos.pop(index)

        with open('todos.txt','w') as file:
            file.writelines(todos)

        message=f"Todo {todo_to_remove}" # as removed from the list
        print(message)

    elif 'exit' in user_action:
        break
print("Bye")












# match case
# while True:
#     user_action=input("Type add,show,edit,complete or exit:")
#     user_action=user_action.strip()

#     match user_action:
#         case 'add':
#             todo=input("Enter a todo:")+"\n"

#             file=open("files/todos.txt",'r')
#             todos=file.readlines()
#             file.close()

#             todos.append(todo)

#             file=open("files/todos.txt",'w')
#             file.writelines(todos)
#             file.close()
#         case 'show':
#             file=open('files/todos.txt','r')
#             todos=file.readlines()
#             file.close()
#             for index,item in enumerate(todos):
#                 row=f"{index+1}={item}"
#                 print(row)
#         case 'edit':
#             number=int(input("Number of the todo to edit"))
#             number=number-1
#             new_todo=input("enter new to do")
#             todos[number]=new_todo
#         case 'complete':
#             number=int(input("Number of the todo to complete"))
#             todos.pop(number-1)
#         case 'exit':
#             break
# # open the file and print the content 
# # with open("bear.txt",'r') as file:
#     # content=file.read()
#     # print(content)
            