FILE_NAME="todos.txt"
def read_todos(filename=FILE_NAME):
    with open(filename, 'r') as file_local:
        read_local = file_local.readlines()
    return read_local
#write function
""" write todos function can be written in several ways"""
"""write_todos function given default argument"""
def write_todos(todos_arg,filename=FILE_NAME):
    with open(filename, 'w') as file_local:
        file_local.writelines(todos_arg)