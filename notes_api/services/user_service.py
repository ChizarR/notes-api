from abc import abstractmethod
from datetime import date
from typing import List

from notes_api.views.note import NoteView


class NotesServiceInterface:
    @abstractmethod
    async def get_notes(self, date: date) -> List[NoteView]:
        raise NotImplementedError("get_notes not implemented")

    @abstractmethod
    async def create_note(self, note: NoteView) -> NoteView:
        raise NotImplementedError("crteate_note not implemented")


class NotesService:
    def __init__(self, dao) -> None:
        self.__dao = dao

    async def get_notes(self, date: date) -> List[NoteView]:
        pass

    async def create_note(self, note: NoteView) -> NoteView:
        pass
