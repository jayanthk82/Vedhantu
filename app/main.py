from fastapi import FastAPI # type: ignore
from .models import NoteSchema
from .database import note_collection
app = FastAPI(title = "Vendhantu API", version ='1.0.0')

@app.get("/")
async def welcome():
    return {"Message":"Your first FAST API endpoint is working"}

@app.post("/notes")
async def add_notes(note : NoteSchema):
    note_dict = note.dict()
    result = await note_collection.insert_one(note_dict)
    return {"status":"Note saved","saved id":str(result.inserted_id)}

