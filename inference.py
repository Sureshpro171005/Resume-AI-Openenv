from fastapi import FastAPI, Request
from env.resume_env import ResumeEnv

app = FastAPI()

env = ResumeEnv(task="medium")


# ✅ ROOT (important)
@app.api_route("/", methods=["GET", "POST"])
async def root(request: Request):
    state = env.reset()
    return {
        "resume": state["resume"],
        "job_description": state["job_description"],
        "score": state["current_score"]
    }



@app.api_route("/reset", methods=["GET", "POST"])
@app.api_route("/reset/", methods=["GET", "POST"])
async def reset(request: Request):
    state = env.reset()
    return {
        "resume": state["resume"],
        "job_description": state["job_description"],
        "score": state["current_score"]
    }



@app.api_route("/step", methods=["POST"])
@app.api_route("/step/", methods=["POST"])
async def step(request: Request):
    data = await request.json()

    action = data.get("action", "add_skills")  # default safe action

    state, reward, done, _ = env.step(action)

    return {
        "resume": state["resume"],
        "score": state["current_score"],
        "reward": reward,
        "done": done
    }