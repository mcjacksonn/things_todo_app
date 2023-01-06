FILEPATH = "todos1.txt"


def get_the_todos(filepath = FILEPATH):
    """ Read a text file and return the list of
    items to-do.
    """
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_the_todos())