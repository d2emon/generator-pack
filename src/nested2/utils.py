import re


CAMEL_CASE = re.compile('([a-z0-9])([A-Z])')


def de_camel_case(s):
    return CAMEL_CASE.sub(r'\1 \2', s).lower()
