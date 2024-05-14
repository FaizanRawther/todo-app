import FreeSimpleGUI as sg
from zip_extractor import extract_archive
sg.theme("Black")


label1=sg.Text("Select Archive")
input1=sg.Input()
choose_button1=sg.FilesBrowse("Choose File", key="archive")

label2=sg.Text("Select Destination")
input2=sg.Input()
choose_button2=sg.FolderBrowse("Choose Folder", key="folder")

extract_button=sg.Button("Extract")
output_label=sg.Text(key="output",text_color="green")

window=sg.Window("Archive Extractor",layout=[[label1,input1,choose_button1],
                                             [label2,input2,choose_button2],
                                             [extract_button],[output_label]])
while True:
    event,value=window.read()
    print(event,value)
    archivePath=value["archive"]
    destinationDirectory=value["folder"]
    extract_archive(archivePath,destinationDirectory)
    window["output"].update(value="Extraction completed")
window.close()