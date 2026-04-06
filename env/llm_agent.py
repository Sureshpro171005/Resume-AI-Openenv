import os
from openai import OpenAI

client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("HF_TOKEN")
)

def improve_resume(resume, job, action):
    prompt = f"""
You are an expert resume optimizer.

Resume:
{resume}

Job Description:
{job}

Action: {action}

Rewrite the resume to better match the job.
Only return the improved resume.
"""

    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content