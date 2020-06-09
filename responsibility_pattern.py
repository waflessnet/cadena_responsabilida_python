from __future__ import annotations
from abc import ABC, abstractmethod
from logging import Handler
from typing import Optional, List


class RequestHandler:
    arr = None
    enriched: List[str] = []

    def __init__(self, arr: List = None, enriched: List[str] = None):
        self.enriched: List[str] = enriched
        self.arr: List = arr


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[None]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: RequestHandler) -> None:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class StepOne(AbstractHandler):
    def handle(self, request: RequestHandler) -> None:
        request.enriched.append('one')
        print(request.enriched)
        super().handle(request)


class StepTwo(AbstractHandler):
    def handle(self, request: RequestHandler) -> None:
        request.enriched.append('two')
        print(request.enriched)
        super().handle(request)


class StepThree(AbstractHandler):
    def handle(self, request: RequestHandler) -> None:
        request.enriched.append('tree')
        print(request.enriched)
        super().handle(request)
