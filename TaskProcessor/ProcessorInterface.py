from Requests.RequestInterface import Request
from WriteManager.ManagerInterface import Manager


class Processor:
    name: str

    def __init__(self, request_generator):
        self.request_generator = request_generator()
        self.managers = []

    def add_manager(self, manager):
        self.managers.append(manager)

    def process(self, response):
        raise NotImplementedError

    def get_required_requests(self, response):
        raise NotImplementedError
