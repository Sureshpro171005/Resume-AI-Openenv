from fastapi import FastAPI, Request
import sys

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
    
    print("[START] task=resume_optimization", flush=True)
    return state

@app.post("/step")
async def step(request: Request):
    try:
        body = await request.json()
        action = body.get("action", "")
        step_num = body.get("step", 1)

        if action:
            state["resume"] = action
        state["score"] = round(state["score"] + 0.1, 2)

        reward = 0.1

        
        print(f"[STEP] step={step_num} reward={reward}", flush=True)

        return {
            "observation": state,
            "reward": reward,
            "done": False,
            "info": {}
        }
    except Exception as e:
        print(f"[STEP] step=0 reward=0.0", flush=True)
        return {
            "observation": state,
            "reward": 0.0,
            "done": False,
            "info": {"error": str(e)}
        }

@app.post("/end")
def end():
    final_score = round(state["score"], 4)
    steps = round((final_score - 0.3) / 0.1)

    
    print(f"[END] task=resume_optimization score={final_score} steps={steps}", flush=True)

    return {"score": final_score}