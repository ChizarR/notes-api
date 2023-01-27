from fastapi import FastAPI

from routes.notes_router import NotesRouter


app = FastAPI()
n_router = NotesRouter()
app.include_router(n_router)


@app.on_event("startup")
async def on_startup() -> None:
    print("Server started")


@app.get("/")
async def test() :
    return {"status": "ok"}
