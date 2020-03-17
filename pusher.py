import config
import subprocess as sp
import datetime


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
    sp.run("git add poem.txt", check=True, shell=True)
    sp.run(f"git commit -m '{config.commit_message}'", check=True, shell=True)
    sp.run("git push -u origin master -f", check=True, shell=True)


def get_pushes_for_day(date=datetime.datetime.now()):
    timedelta = date - config.start_date
    week = (timedelta.days + (config.start_date.weekday() + 1) % 7) // 7
    weekday = (date.weekday() + 1) % 7
    if weekday >= len(config.image) or week >= len(config.image[weekday]):
        return 0
        # TODO notify
    return config.image[weekday][week]


if __name__ == "__main__":
    for i in range(get_pushes_for_day()):
        write_new_line()
        push_text()
