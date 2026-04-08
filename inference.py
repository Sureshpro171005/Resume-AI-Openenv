from fastapi import FastAPI, Request

app = FastAPI()

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
    return state

@app.post("/step")
async def step(request: Request):
    try:
        body = await request.json()
        action = body.get("action", "")

        if action:
            state["resume"] = action

        state["score"] = round(state["score"] + 0.1, 2)

        return {
            "observation": state,
            "reward": 0.1,
            "done": False,
            "info": {}
        }

    except Exception as e:
        return {
            "observation": state,
            "reward": 0.0,
            "done": False,
            "info": {"error": str(e)}
        }