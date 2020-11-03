class BaseService:
    def __init__(self, cache):
        raise NotImplementedError

    def start(self, cache):
        raise NotImplementedError
