import re


CAMEL_CASE = re.compile('([a-z0-9])([A-Z])')


def camel_case_to_spaces(name):
    return CAMEL_CASE.sub(r'\1 \2', name).lower()
