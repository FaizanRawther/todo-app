import FreeSimpleGUI as fsg
from converter import convertFeetInches_to_Meters
feet_label=fsg.Text("Enter Feet: ")
feet_input=fsg.Input(key="feet")

inch_label=fsg.Text("Enter inches: ")
inch_input=fsg.Input(key="inch")

button_convert=fsg.Button("Convert")
output_label=fsg.Text("",key="output")

exit_button=fsg.Button("Exit")

fsg.theme("Black")

window=fsg.Window("Converter",
                  layout=[[feet_label,feet_input],
                          [inch_label,inch_input]
                          ,[button_convert,output_label,exit_button]])


while True:
    try:
        event, values=window.read()
        print(event,values)
        feet=float(values["feet"])
        inches=float(values["inch"])
        result=convertFeetInches_to_Meters(feet,inches)
        window["output"].update(value=f"{result} m", text_color="white")
    except ValueError:
        print("You have exited program")
    match event:
        case fsg.WIN_CLOSED:
            break
        case "Exit":
            break
window.close()