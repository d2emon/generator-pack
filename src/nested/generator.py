import re


CAMEL_CASE = re.compile('([a-z0-9])([A-Z])')


def camel_case_to_spaces(s):
    return CAMEL_CASE.sub(r'\1 \2', s).lower()


class Generated:
    type_name = None
    subgenerators = []
    names_data = []

    def __init__(self, name=None):
        self.__template_name = ""
        self.name = name or self.template_name

    @property
    def template_name(self):
        if self.__template_name is not None:
            return self.__template_name

        self.__template_name = self.type_name or camel_case_to_spaces(type(self).__name__)
        return self.__template_name

    @classmethod
    def generate(cls):
        pass