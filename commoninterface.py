#from functions import get_the_todos, write_todos
import functions
import time

date = time.strftime("%b %d,%Y %H:%M:%S")
print(date)
while True :
    action = input("add an item, show list, edit list, mark item completed,or exit:")
    action = action.strip()

    if action.startswith("add"):
        todo1 = action[4:]

        todos = functions.get_the_todos()

        todos.append(todo1 + '\n')

        functions.write_todos(todos)

    elif action.startswith("show"):
        todos = functions.get_the_todos()

        for index, items in enumerate(todos):
            item = items.strip('\n')
            row = f"{index + 1}-{items}"
            print(row)
    elif action.startswith("edit"):
        try:
            number = int(action[5:])
            print(number)

            number = number - 1

            todos = functions.get_the_todos()

            new_todo = input("Enter new item todo: ")
            todos[number] = new_todo + '\n'


            with open('venv/todos1.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif action.startswith("completed" or "complete"):
        try:
            number = int(action[9:])

            todos = functions.get_the_todos()
            index = number - 1
            to_remove_todo = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"The Todo {to_remove_todo} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number: ")

    elif action.startswith("exit"):
            break
    else:
        print("Your command is not a valid command")


print("Goodbye!")








