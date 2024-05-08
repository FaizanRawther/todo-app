import FreeSimpleGUI as fsg

import functions
import functions as func
label=fsg.Text("Type in to-do")
input_box=fsg.InputText(tooltip="Enter Todo",key='todo')
add_button=fsg.Button("Add")

list_box=fsg.Listbox(values=func.read_todos(),
                     key='todos',
                     enable_events=True, size=[45,10])
edit_button=fsg.Button("Edit")
complete_button=fsg.Button("Complete")
exit_button=fsg.Button("Exit")

window=fsg.Window("My Todo App",
                  layout=[[[label],
                           [input_box,add_button],[list_box,edit_button,complete_button],[exit_button]]],
                  font=('helvetica',14))
while True:
    event,values=window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":
            todos=func.read_todos()
            new_todos=values['todo'] + "\n"
            todos.append(new_todos)
            func.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit=values['todos'][0]
            new_todo=values['todo']
            todos=func.read_todos()
            index=todos.index(todo_to_edit)
            todos[index]=new_todo
            func.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todo_to_complete=values['todos'][0]
            todos=functions.read_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case fsg.WIN_CLOSED:
            break

window.close()
