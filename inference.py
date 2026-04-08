from fastapi import FastAPI, Request
import uvicorn
import threading
import requests
import time

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


def run_evaluation():
    # Wait for server to be ready
    time.sleep(3)

    base_url = "http://0.0.0.0:7860"
    task_name = "resume_optimization"
    num_steps = 5

    print(f"[START] task={task_name}", flush=True)

    # Reset environment
    requests.post(f"{base_url}/reset")

    total_reward = 0.0
    for i in range(1, num_steps + 1):
        response = requests.post(f"{base_url}/step", json={"action": f"optimized_resume_step_{i}"})
        result = response.json()
        reward = result.get("reward", 0.0)
        total_reward += reward
        print(f"[STEP] step={i} reward={reward}", flush=True)

    final_score = round(total_reward, 4)
    print(f"[END] task={task_name} score={final_score} steps={num_steps}", flush=True)


if __name__ == "__main__":
    # Run evaluation in background thread after server starts
    eval_thread = threading.Thread(target=run_evaluation, daemon=True)
    eval_thread.start()

    uvicorn.run(app, host="0.0.0.0", port=7860)