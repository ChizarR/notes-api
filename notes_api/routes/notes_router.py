from datetime import date
from typing import Dict

from fastapi import APIRouter
from notes_api.services.user_service import NotesServiceInterface

from notes_api.views.note import NoteView


class NotesRouter:
    def __init__(self) -> None:
        self._router = APIRouter(prefix="notes")
        self._service: NotesServiceInterface

        self.register_endpoints()

    @property
    def router(self) -> APIRouter:
        return self._router

    def register_endpoints(self) -> None:
        self._router.add_api_route("/test", self.test, status_code=200)

        self._router.add_api_route("/get/{date}", self.get_notes, status_code=200)
        self._router.add_api_route("/create", self.create_note, status_code=201)

    async def test(self) -> Dict:
        return {"ok": True}

    async def get_notes(self, date: date):
        pass

    async def create_note(self, note: NoteView):
        pass
