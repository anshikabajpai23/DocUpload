from typing import Optional
from pydantic import BaseModel, Field

# Notebook models
class NotebookCreate(BaseModel):
    name: str = Field(..., description="Name of the notebook")
    description: str = Field(default="", description="Description of the notebook")


class NotebookUpdate(BaseModel):
    name: Optional[str] = Field(None, description="Name of the notebook")
    description: Optional[str] = Field(None, description="Description of the notebook")

class NotebookResponse(BaseModel):
    id: int
    name: str
    description: str