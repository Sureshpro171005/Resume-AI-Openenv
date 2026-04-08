from fastapi import FastAPI, Request


app = FastAPI()

# Global state
state = {
    "resume": "sample resume",
    "job_description": "sample job",
    "score": 0.3
}

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/reset")
def reset():
    global state
    state = {
        "resume": "sample resume",
        "job_description": "sample job",
        "score": 0.3
    }
    return state   # return the reset state

@app.post("/step")
async def step(request: Request):
    body = await request.json()

    action = body.get("action", "")

    # Update state based on action
    state["resume"] = action if action else state["resume"]
    state["score"] = round(state["score"] + 0.1, 2)

    return {
        "observation": state,
        "reward": 0.1,
        "done": False,
        "info": {}
    }
