import functions
import PySimpleGUI as psg
import time
import os

if not os.path.exists("todos1.txt"):
    with open("todos1.txt", "w") as file:
        pass

psg.theme("Black")

watch = psg.Text('', key='clock')
words = psg.Text("Enter a to-do item")
box_input = psg.InputText(tooltip="Type todo", key="todo")
button_add = psg.Button(size=3, image_source="add.png", mouseover_colors="LightBlue2",
                        tooltip= "Add todo item", key="Add")
list_for_box = psg.Listbox(values=functions.get_the_todos(), key='todos',
                           enable_events = True, size=[45,10])
button_edit = psg.Button("Edit")
button_complete = psg.Button(size=3, image_source = "complete.png", mouseover_colors="LightBlue2",
                            tooltip="Completed todo item", key= "Complete")
button_exit = psg.Button("Exit")

window = psg.Window("My To-Do List",
                    layout=[[watch],
                            [words],
                            [box_input], [button_add],
                            [list_for_box,button_edit, button_complete],
                            [button_exit]],
                    font=('Helvetica',20))
while True:
    action, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d,%Y %H:%M:%S"))
    print(1, action)
    print(2, values)
    print(3, values['todos'])
    match action:
        case "Add":
            todos = functions.get_the_todos()
            todo_new = values['todo'] + "\n"
            todos.append(todo_new)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                to_edit_todo = values['todos'][0]
                todo_new = values['todo']

                todos = functions.get_the_todos()
                index = todos.index(to_edit_todo)
                todos[index] = todo_new
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                psg.popup("Please select an item first", font=("Helvetica", 20))
        case "Complete":
          try:
            to_complete_todo = values['todos'][0]
            todos = functions.get_the_todos()
            todos.remove(to_complete_todo)
            functions.write_todos((todos))
            window['todos'].update(values=todos)
            window['todo'].update(value='')
          except IndexError:
            psg.popup("Please select an item first", font=("Helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case psg.WINDOW_CLOSED:
            break


window.close()


