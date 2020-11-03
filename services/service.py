"""
Base implementation for microservice architecture
"""
from flask import Flask
from multiprocessing import Process, Manager
import response


class Service:
    """
    Service wrapper for Microservice built with Flask
    """
    app = Flask(__name__)
    service = None

    class Bound:
        """
        Bound class to Service object, links callable to Flask
        """
        service = None

        def __init__(self, action, cache):
            self.manager = Manager()
            self.action = action
            self.cache = self.manager.dict(cache)
            self.process = Process(target=self.action, args=(self.cache,))
            self.response = response.CustomResponse()

        def __call__(self, *args):
            # Only one process per service per fetch
            try:
                self.process.start()
            except AssertionError as e:
                self.cache['process_is_alive'] = self.process.is_alive()
                return self.response.send_status('BUSY', self.cache.copy())

            return self.response.send_status('INIT', self.cache.copy())

    def __init__(self, name, endpoint, action, cache):
        self.name = name
        self.endpoint = endpoint
        self.bound = self.Bound(action, cache)
        self.app.add_url_rule(self.endpoint, self.name, self.bound)

    def start(self):
        self.app.run(debug=True)
