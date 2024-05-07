import FreeSimpleGUI as fsg
label1=fsg.Text("Enter Feet: ")
input_text1=fsg.Input()

label2=fsg.Text("Enter inches: ")
input_text2=fsg.Input()

button_convert=fsg.Button("Convert")

window=fsg.Window("Converter",
                  layout=[[label1,input_text1],
                          [label2,input_text2]
                          ,[button_convert]])
window.read()
window.close()