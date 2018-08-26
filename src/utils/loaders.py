import os


ROOT_PATH = os.path.abspath(os.path.join(os.path.curdir))


def load_lines(filename):
    """
    Load file as array of lines
    :param filename:
    :return:
    """
    full_filename = os.path.join(ROOT_PATH, filename)

    lines = []
    with open(full_filename, "r", encoding='utf-8') as f:
        lines = [line.strip() for line in f]
    return lines


def load_text(filename):
    """
    Load file as plain text
    :param filename:
    :return:
    """
    return "\n".join(load_lines(filename))