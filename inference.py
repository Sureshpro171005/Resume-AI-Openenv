from fastapi import FastAPI, Request
from env.resume_env import ResumeEnv
import uvicorn

app = FastAPI()

env = ResumeEnv(task="medium")


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



@app.api_route("/step", methods=["GET", "POST"])
@app.api_route("/step/", methods=["GET", "POST"])
async def step(request: Request):
    try:
        data = await request.json()
    except:
        data = {}

    action = data.get("action", "add_skills")

    state, reward, done, _ = env.step(action)

    return {
        "resume": state["resume"],
        "score": state["current_score"],
        "reward": reward,
        "done": done
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)