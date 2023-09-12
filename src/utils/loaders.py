def load_lines(filename):
    """
    Load file as array of lines
    :param filename:
    :return:
    """
    with open(filename, "r", encoding='utf-8') as f:
        for line in f:
            yield line.strip()


def load_text(filename):
    """
    Load file as plain text
    :param filename:
    :return:
    """
    return "\n".join(load_lines(filename))
