from __future__ import annotations
from abc import ABC, abstractmethod
from logging import Handler
from typing import Optional, Any, List


class RequestHandler:
    arr = None  # only learning
    enriched: List[str] = []

    def __init__(self, arr: List, enriched: List[str]):
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
        print('one')
        request.enriched.append('paso 1')
        super().handle(request)


class StepTwo(AbstractHandler):
    def handle(self, request: RequestHandler) -> None:
        print('two')
        request.enriched.append('paso 2')
        super().handle(request)


class StepThree(AbstractHandler):
    def handle(self, request: RequestHandler) -> None:
        print('three')
        request.enriched.append('paso 3')
        super().handle(request)
