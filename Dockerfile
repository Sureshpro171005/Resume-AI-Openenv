FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Allow the runner to choose a free port via $PORT.
# If the runner doesn't provide PORT, fall back to 7860 for local usage.
ENV PORT=7860
CMD ["sh", "-c", "uvicorn inference:app --host 0.0.0.0 --port ${PORT:-7860}"]