import config
from string import digits, punctuation
import re
from statistics import mean


def is_roman(s):
    thousand = 'M{0,3}'
    hundred = '(C[MD]|D?C{0,3})'
    ten = '(X[CL]|L?X{0,3})'
    digit = '(I[VX]|V?I{0,3})'
    return bool(re.match(thousand + hundred + ten + digit + '$', s))


def get_lines(path):
    with open(path, "r") as file:
        return file.readlines()


def clean_text(path):
    text = get_lines(path)
    text = [l.strip().replace("·", "") for l in text if len(l.strip().replace("·", "")) > 0]

    # Get the table to remove its contents from the body
    table_ind = text.index("TABLE")
    table = text[table_ind:]
    table = [l.translate(str.maketrans('', '', digits)).strip() for l in table]
    to_delete = set()
    for line in table:
        line = line.split(" ", 1)
        if len(line) > 1:
            if is_roman(line[0]):
                to_delete.add(line[0])
                if line[1].isupper():
                    to_delete.add(line[1])
            else:

                to_delete.add(" ".join(line).strip(punctuation))
        else:
            to_delete.add(line[0])

    # Clean the text body
    text = text[:table_ind]
    final_text = list()
    for line in text:
        if len(line) > 0 \
                and not line.isupper() \
                and not any(char.isdigit() for char in line) \
                and line not in to_delete:
            final_text.append(line)

    return final_text


def combine_texts(path1, path2):
    text1 = clean_text(path1)
    print(f"Text 1 has {len(text1)} lines")
    text2 = clean_text(path2)
    print(f"Text 2 has {len(text2)} lines")
    text1.extend(text2)
    print(f"Final text has has {len(text1)} lines")
    return text1


def save_to_file(text):
    with open(config.clean_txt_path, "w") as file:
        file.write("\n".join(text))
        print(f"Wrote to file at {config.clean_txt_path.as_posix()}")


def get_avg_length(text):
    lengths = [len(line.split()) for line in text]
    print(f"The average number of words of a line is {int(mean(lengths))}")


if __name__ == "__main__":
    text = combine_texts(config.txt_1_path, config.txt_2_path)
    get_avg_length(text)
    save_to_file(text)
