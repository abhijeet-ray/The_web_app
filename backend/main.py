from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from questions import InterviewQuestionProvider

app = FastAPI()

# CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the question provider
provider = InterviewQuestionProvider()


class InterviewRequest(BaseModel):
    profile: str
    experience: str  # Matches your frontend's "experience" parameter


@app.post("/get-questions/")
async def get_questions(request: InterviewRequest):
    questions = provider.get_questions(request.profile, request.experience)
    if isinstance(questions, str):  # Handle error case
        raise HTTPException(status_code=400, detail=questions)
    return {"questions": questions}
