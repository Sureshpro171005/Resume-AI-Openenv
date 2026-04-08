from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "ok"}


@app.post("/reset")
def reset():
    return {"status": "reset ok"}


def main():
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()