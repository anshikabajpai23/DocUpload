from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter
from Notebook import Notebook
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

@app.post("/mynotebook")
def create_notebook(
        name: str,
        description: str
):

    mynotebook= Notebook(name,description)
    val = mynotebook.print_all()
    return val








