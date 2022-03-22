from v1.fixtures import genders
from v1.factories.fng.data_factory import FactoriesBlock
from v1.factories.fng.name_factory import NameFactory
from v1.models.fng.description import Mark, MarkDescription


class MarksFactories(FactoriesBlock):
    @property
    def mark_start_factory(self):
        return self.factory('mark_start')

    @property
    def mark_middle_factory(self):
        return self.factory('mark_middle')

    @property
    def mark_finish_factory(self):
        return self.factory('mark_finish')

    @property
    def mark_memory_factory(self):
        return self.factory('mark_memory')

    @property
    def mark_subject_factory(self):
        return self.factory('mark_subject')

    @property
    def description_factory(self):
        def f(*args, gender_id=None, **kwargs):
            return MarkDescription(
                mark=self.model,  # 12
                start=self.mark_start_factory(gender_id=gender_id),  # 13
                middle=self.mark_middle_factory(gender_id=gender_id),  # 14
                finish=self.mark_finish_factory(gender_id=gender_id),  # 15
                memory=self.mark_memory_factory(gender_id=gender_id),  # 16
                subject=self.mark_subject_factory(gender_id=gender_id),  # 17
            )
        return f


class MarksFactory(NameFactory):
    child_class = Mark
    group_id = "mark"

    def get_value(self, *args, gender_id=genders.NEUTRAL, **kwargs):
        items = self.factories.filtered(
            group_id=self.group_id,
            gender_id=gender_id,
        )
        return next(items)

    def get_child(self, value):
        item = self.child_class(value)
        item.factories = MarksFactories(
            item,
            self.factories,
        )
        return item
