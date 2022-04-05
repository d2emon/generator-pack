class Gender:
    name = ''


    @property
    def body(self):
        return self.url('body')

    def url(self, item):
        raise NotImplementedError()


class Male(Gender):
    name = 'Male'

    def url(self, item):
        return "../images/armor/male/{}.png".format(item)


class Female(Gender):
    name = 'Female'

    def url(self, item):
        return "../images/armor/female/{}.png".format(item)
