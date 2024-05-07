import FreeSimpleGUI as fsg
import functions as func
label=fsg.Text("Type in to-do")
input_box=fsg.InputText(tooltip="Enter Todo")
add_button=fsg.Button("Add")
exit=fsg.qu
window=fsg.Window("My Todo App",layout=[[[label],[input_box,add_button],[exit]]])
window.read()
window.close()
