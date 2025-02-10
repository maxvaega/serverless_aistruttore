from pydantic import BaseModel, Field
from typing import Optional

# Define response model

class MessageRequest(BaseModel):
    message: str
    userid: str = Field(..., min_length = 1)

class MessageResponse(BaseModel):
    query: str
    result: str
    userid: str = Field(..., min_length = 1)

