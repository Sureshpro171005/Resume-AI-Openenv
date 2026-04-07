from fastapi import FastAPI, Request
from pydantic import BaseModel
from env.resume_env import ResumeEnv

app = FastAPI()

env = ResumeEnv(task="medium")

class ActionRequest(BaseModel):
    action: str


@app.api_route("/", methods=["GET", "POST"])
def root():
    state = env.reset()
    return {
        "resume": state["resume"],
        "job_description": state["job_description"],
        "score": state["current_score"]
    }



@app.api_route("/reset", methods=["GET", "POST"])
@app.api_route("/reset/", methods=["GET", "POST"])
def reset():
    state = env.reset()
    return {
        "resume": state["resume"],
        "job_description": state["job_description"],
        "score": state["current_score"]
    }



@app.api_route("/step", methods=["POST"])
@app.api_route("/step/", methods=["POST"])
def step(req: ActionRequest):
    state, reward, done, _ = env.step(req.action)

    return {
        "resume": state["resume"],
        "score": state["current_score"],
        "reward": reward,
        "done": done
    }