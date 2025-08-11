from fastapi import FastAPI
from fastapi import APIRouter
from Notebook import Notebook
from models import *
from db import cur
router = APIRouter()

app=FastAPI(
    title="NOTEBOOK LM COPY",
    description="Document upload assistant"

)

# app.add_middleware(CORSMiddleware,
#                    allow_origins=["*"],
#                    allow_headers=["*"],
#                    allow_credentials=["*"],
#                    allowe_methods=["*"]
#                    )

@app.post("/myNotebook", response_model=NotebookCreate)
def create_notebook(notebook: NotebookCreate):

    new_notebook = Notebook(name = notebook.name,
                            description=notebook.description)
    cur.insert_one(new_notebook)
    return NotebookResponse(
        id=new_notebook.id,
        name=new_notebook.name,
        description=new_notebook.description)

@app.get("/myNotebook/{id}", response_model=NotebookCreate)
def get_notebook(id: int):


    new_notebook=cur.fetchone(id)
    return NotebookResponse(
        id=new_notebook.id,
        name=new_notebook.name,
        description=new_notebook.description)


@app.patch("/myNotebook/{id}", response_model=NotebookCreate)
def update_notebook(id: int, notebook: NotebookCreate):
    new_notebook = cur.fetchone(id)

    return NotebookResponse(
        id = new_notebook.id,
        name=new_notebook.name,
        description=new_notebook.description)


@app.delete("/myNotebook/{id}")
def delete_notebook(id: int):
    cur.execute("DELETE FROM notebook WHERE id = ?", [id])
    return "ok"









