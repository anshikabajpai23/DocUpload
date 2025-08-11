import uuid
from typing import Optional

from models import NotebookResponse


class Notebook:
    id: Optional[int] = 0
    name: str
    description: str
    def __init__(self,
                 name,
                 description):
        self.id = self.id+1
        self.name = name
        self.description = description

    def print_all(self):
        return (f"name: {self.name} and description: {self.description}")

    def get(self) -> NotebookResponse:
        return NotebookResponse(name = self.name, description=self.description,id = self.id)
