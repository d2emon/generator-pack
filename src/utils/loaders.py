import config
import os


def load_lines(filename):
    """
    Load file as array of lines
    :param filename:
    :return:
    """
    full_filename = os.path.join(config.CURRENT_PATH, filename)

    with open(full_filename, "r", encoding='utf-8') as f:
        for line in f:
            yield line.strip()


def load_text(filename):
    """
    Load file as plain text
    :param filename:
    :return:
    """
    return "\n".join(load_lines(filename))
