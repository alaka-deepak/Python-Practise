user_prompt="Enter a todo:"

# While Loop -Infinite - 1st condition
# while True:
#     todo=input(user_prompt)
#     print(todo)

# 2nd condition
# while True: 
#     todo=input(user_prompt)
#     todos=[todo]#Overwrite the list in each loop
#     print(todos)

todos=[]
while True:
    todo=input(user_prompt)
    todos.append(todo)
    print(todos)