from fastapi import FastAPI, Request
import os

app = FastAPI()

# Global state
state = {
    "resume": "sample resume",
    "job_description": "sample job",
    "score": 0.3
}

# Health check
@app.get("/")
def health():
    return {"status": "ok"}

# Reset endpoint
@app.post("/reset")
def reset():
    global state
    state = {
        "resume": "sample resume",
        "job_description": "sample job",
        "score": 0.3
    }
    return state

# Step endpoint
@app.post("/step")
async def step(request: Request):
    try:
        body = await request.json()
        action = body.get("action", "")

        # Update state
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

# IMPORTANT: Dynamic port binding (fixes your error)
if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)