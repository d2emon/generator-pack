def load_lines(filename):
    lines = []
    with open(filename, "r", encoding='utf-8') as f:
        lines = [line.strip() for line in f]
    return lines


def load_text(filename):
    return "\n".join(load_lines(filename))