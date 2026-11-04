"""In-memory FastAPI implementation of the Notes API."""

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field


class NoteInput(BaseModel):
    """Fields supplied when creating or replacing a note."""

    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)


class Note(NoteInput):
    """A note with its server-assigned identifier."""

    id: int


app = FastAPI(title="Notes API", version="0.1.0")

_notes: dict[int, Note] = {}
_next_id = 1


def note_or_404(note_id: int) -> Note:
    note = _notes.get(note_id)
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note {note_id} was not found",
        )
    return note


@app.get("/notes", response_model=list[Note])
def list_notes() -> list[Note]:
    """Return all notes in ascending identifier order."""

    return [_notes[note_id] for note_id in sorted(_notes)]


@app.post("/notes", response_model=Note, status_code=status.HTTP_201_CREATED)
def create_note(note_input: NoteInput) -> Note:
    """Create a note and assign it the next available identifier."""

    global _next_id

    note = Note(id=_next_id, **note_input.model_dump())
    _notes[note.id] = note
    _next_id += 1
    return note


@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int) -> Note:
    """Return one note by identifier."""

    return note_or_404(note_id)


@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, note_input: NoteInput) -> Note:
    """Replace the title and content of an existing note."""

    note_or_404(note_id)
    updated_note = Note(id=note_id, **note_input.model_dump())
    _notes[note_id] = updated_note
    return updated_note


@app.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int) -> Response:
    """Delete one note."""

    note_or_404(note_id)
    del _notes[note_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
