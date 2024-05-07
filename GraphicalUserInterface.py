import FreeSimpleGUI as fsg
import functions as func
label=fsg.Text("Type in to-do")
input_box=fsg.InputText(tooltip="Enter Todo",key='todos')
add_button=fsg.Button("Add")

window=fsg.Window("My Todo App",
                  layout=[[[label],
                           [input_box,add_button]]],
                  font=('helvetica',14))
while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos=func.read_todos()
            new_todos=values['todos'] + "\n"
            todos.append(new_todos)
            func.write_todos(todos)
        case fsg.WIN_CLOSED:
            break

window.close()
