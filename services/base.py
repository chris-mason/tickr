class BaseService:
    def __init__(self, cache):
        self.cache = cache

    def start(self, cache):
        raise NotImplementedError
