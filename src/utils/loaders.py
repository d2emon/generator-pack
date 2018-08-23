def load_lines(filename):
    """
    Load file as array of lines
    :param filename:
    :return:
    """
    lines = []
    with open('../' + filename, "r", encoding='utf-8') as f:
        lines = [line.strip() for line in f]
    return lines


def load_text(filename):
    """
    Load file as plain text
    :param filename:
    :return:
    """
    return "\n".join(load_lines(filename))