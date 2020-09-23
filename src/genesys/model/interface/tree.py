class TreeModelInterface:
    @property
    def children(self):
        """
        Add all children from generate_children() and shuffle them

        :return: Model children
        """
        raise NotImplementedError()

    @property
    def parent(self):
        """
        :return: Model parent
        """
        raise NotImplementedError()

    @parent.setter
    def parent(self, value):
        """
        Sets model parent

        :param value:
        :return:
        """
        raise NotImplementedError()

    def add_child(self, child):
        """
        Add child to children and set child parent

        :param child:
        """
        raise NotImplementedError()
