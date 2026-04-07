from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

# dummy state
state = {
    "resume": "sample resume",
    "job_description": "sample job",
    "score": 0.3
}

@app.post("/")
@app.post("/reset")
def reset():
    return state

@app.post("/step")
async def step(request: Request):
    return {
        "resume": "updated resume",
        "score": 0.4,
        "reward": 0.1,
        "done": False
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)