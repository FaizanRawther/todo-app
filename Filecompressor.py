import FreeSimpleGUI as fsg
from ZipCreater import make_archive
label1=fsg.Text("Select files to compress: ")
input1=fsg.Input()
choose_button1=fsg.FilesBrowse("Choose",key="Files")

label2=fsg.Text("Select the destination folder: ")
input2=fsg.Input()
choose_button2=fsg.FolderBrowse("Choose",key="Folder")

compress_button=fsg.Button("Compress")

output_label=fsg.Text(key="output",text_color="green")

window=fsg.Window("File Compressor",
                  layout=[[label1,input1,choose_button1],
                          [label2,input2,choose_button2],
                          [compress_button],
                          [output_label]])
while True:
    event,values=window.read()
    print(event,values)
    filepaths=values["Files"].split(";")
    folder=values["Folder"]
    make_archive(filepaths,folder)
    window["output"].update(value="compression completed")
    match event:
        case fsg.WIN_CLOSED:
            break
window.close()