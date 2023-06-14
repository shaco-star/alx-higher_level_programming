#!/usr/bin/python3

"""Define Function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line into a file after each line containing a specific string.

    :param filename: The name of the file to modify.
    :param search_string: The string to search for in the file.
    :param new_string: The string to insert into the file.
    """
    new_lines = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string + "\n")

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
