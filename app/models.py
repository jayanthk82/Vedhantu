from pydantic import BaseModel,Field #type: ignore
from bson import ObjectId #type: ignore
class NoteSchema(BaseModel):
    user_id : str
    content : str = Field(...,min_length = 10)
    ease_factor : float = 2.5
    interval : int = 0
    repetitions : int = 0

    class Config:
        arbitrary_types_allowed = True 
        json_encoders = {ObjectId: str}
