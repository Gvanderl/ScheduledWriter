import config
import subprocess as sp
import datetime
from pathlib import Path
from writer import learn_and_write


def get_new_line():
    return learn_and_write() + "\n"


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
    git_dir = Path(__file__).resolve().parent / ".git"
    sp.run(f"git --git-dir {git_dir} add {git_dir.parent / 'poem.txt'}", check=True, shell=True)
    sp.run(f"git --git-dir {git_dir} commit -m 'The poem grows'", check=True, shell=True)
    sp.run(f"git --git-dir {git_dir} push -u origin master -f", check=True, shell=True)
    print("Pushed to master")


def get_pushes_for_day(date=datetime.datetime.now()):
    timedelta = date - config.start_date
    week = (timedelta.days + (config.start_date.weekday() + 1) % 7) // 7
    weekday = (date.weekday() + 1) % 7
    if weekday >= len(config.image) or week >= len(config.image[weekday]):
        print("Ran out of bounds")
        return 0
        # TODO notify
    return config.image[weekday][week]


if __name__ == "__main__":
    write_new_line()
    push_text()
