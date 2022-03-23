class ProviderFactory:
    def __call__(self):
        raise NotImplementedError()

    def __iter__(self):
        return self

    def __next__(self):
        return self()

    # TODO: Restore add function for provider
