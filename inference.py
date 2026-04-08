from fastapi import FastAPI, Request
import uvicorn

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
    return {"status": "reset successful"}

@app.post("/step")
async def step(request: Request):
    global state
    try:
        body = await request.json()

        # Safe extraction
        action = body.get("action", "")

        # Update state
        if isinstance(action, str) and action:
            state["resume"] = action

        state["score"] = round(state["score"] + 0.1, 2)

        return {
            "observation": str(state),  # ✅ MUST be string
            "reward": float(0.1),       # ✅ ensure float
            "done": False,
            "info": {}
        }

    except Exception as e:
        return {
            "observation": str(state),
            "reward": 0.0,
            "done": False,
            "info": {"error": str(e)}
        }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)