from fastapi import FastAPI
from pydantic import BaseModel
from env.resume_env import ResumeEnv

app = FastAPI()

env = ResumeEnv(task="medium")

class ActionRequest(BaseModel):
    action: str



@app.post("/")
def root_reset():
    state = env.reset()
    return {
        "resume": state["resume"],
        "job_description": state["job_description"],
        "score": state["current_score"]
    }



@app.post("/reset")
def reset():
    state = env.reset()
    return {
        "resume": state["resume"],
        "job_description": state["job_description"],
        "score": state["current_score"]
    }


@app.post("/step")
def step(req: ActionRequest):
    state, reward, done, _ = env.step(req.action)

    return {
        "resume": state["resume"],
        "score": state["current_score"],
        "reward": reward,
        "done": done
    }