from fastapi import FastAPI, HTTPException
from app.models.models import Notes
app = FastAPI(
    title="Secure Notes Security Lab",
    description="A security-focused notes API",
    version ="0.1.0",
)
notes_db = []

@app.get("/")

async def root():
    return {"message": "Secure Notes API is runnuing"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/notes", status_code=201)
async def create_note(note: Notes):
    new_note = {
        "id": len(notes_db)+1,
        "title": note.title,
        "content": note.content
    }
    notes_db.append(new_note)
    return new_note

@app.get("/notes/{notes_id}")
async def get_note(notes_id: int):
    for note in notes_db:
        if note["id"] == notes_id:
            return note

    raise HTTPException(status_code=404, detail="Note not found")

@app.delete("/delete_note")
async def delete_notes(notes_id: int):
    for note in notes_db:
        if note["id"] == notes_id:
            notes_db.remove(note)
            return {"status": True}
    return {HTTPException(status_code=404, detail="note not found")}