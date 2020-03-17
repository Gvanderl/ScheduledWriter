import config
import secret_stuff
import subprocess as sp

def get_new_line():
    return "Temporary\n"


def write_to_file(text):
    with open(config.file_path, "a+") as file:
        file.write(text)


def get_text():
    with open(config.file_path, "r") as file:
        return file.read()


def write_new_line():
    new_line = get_new_line()
    print(f"Adding to the poem :\n{new_line}")
    write_to_file(new_line)
    print(f"Poem is now:\n{get_text()}")


def push_text():
    sp.run("")

if __name__=="__main__":
    write_new_line()
    push_text()