from ..factory import Factory


class DelegatorFactory(Factory):
    def __init__(self, factory, **options):
        """
        Construct factory with data from database.

        Args:
            data (Database, optional): Database for factory. Defaults to None.
        """
        super().__init__(**options)
        self.factory = factory

    def __call__(
        self,
        *args,
        **kwargs,
    ):
        """Build some models

        Args:
            count (int, optional): Pregenerated models count. Defaults to None.

        Yields:
            Model: Generated model
        """
        self.logger.debug('Create single instance of %s', self.factory)
        yield self.factory(
            *args,
            **kwargs,
        )
