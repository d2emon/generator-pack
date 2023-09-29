from ..factory import Factory


class DelegatorFactory(Factory):
    @property
    def factory(self):
        return self.data

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
