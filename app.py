from fastapi import FastAPI, HTTPException
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
async def create_notebook(notebook: NotebookCreate):

    new_notebook = Notebook(name = notebook.name,
                            description=notebook.description)
    cur.execute("INSERT INTO notebook (name, description) VALUES (?, ?)",
                [new_notebook.name, new_notebook.description])
    return NotebookResponse(
        id=new_notebook.id,
        name=new_notebook.name,
        description=new_notebook.description)

@app.get("/myNotebook/{id}", response_model=NotebookCreate)
async def get_notebook(id: int):


    new_notebook=cur.execute("SELECT * FROM notebook WHERE id = ?", [id]).fetchone()
    if new_notebook is None:
        raise HTTPException(status_code=404, detail="Notebook not found")
    return NotebookResponse(
        id=new_notebook[0],
        name=new_notebook[1],
        description=new_notebook[2])


@app.patch("/myNotebook/{id}", response_model=NotebookCreate)
async def update_notebook(id: int, notebook: NotebookCreate):
    new_notebook=cur.execute("SELECT * FROM notebook WHERE id = ?", [id]).fetchone()
    if new_notebook is None:
        raise HTTPException(status_code=404, detail="Notebook not found")
    updated_notebook = NotebookUpdate(name=notebook.name, description=notebook.description)
    cur.execute("UPDATE notebook SET name = ?, description = ? WHERE id = ?", 
                [updated_notebook.name, updated_notebook.description, id])
    return NotebookResponse(
        id=id,
        name=new_notebook.name,
        description=new_notebook.description)


@app.delete("/myNotebook/{id}")
async def delete_notebook(id: int):
    new_notebook=cur.execute("SELECT * FROM notebook WHERE id = ?", [id]).fetchone()
    if new_notebook is None:
        raise HTTPException(status_code=404, detail="Notebook not found")
    cur.execute("DELETE FROM notebook WHERE id = ?", [id])
    return "ok"









