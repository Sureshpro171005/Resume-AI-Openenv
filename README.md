---

title: Resume AI OpenEnv
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
app_file: app.py
pinned: false
-------------

# 🤖 Resume AI OpenEnv

An AI-powered environment where an intelligent agent improves resumes step-by-step to better match job descriptions using reward-based learning.

---

## 🚀 Overview

This project simulates a real-world resume optimization system.
An AI agent analyzes a resume and iteratively improves it to maximize job relevance and ATS compatibility.

---

## 🎯 Key Features

* OpenEnv compliant (`reset`, `step`, `state`)
* AI agent improves resume iteratively
* Reward-based scoring system (0.0 → 1.0)
* Semantic similarity matching
* 3 difficulty levels: Easy, Medium, Hard
* Reproducible inference pipeline
* Gradio-based UI

---

## 🧠 How It Works

1. Initialize environment with a resume
2. Agent performs actions:

   * Add relevant skills
   * Improve experience
   * Optimize keywords
3. Each step updates score and resume
4. Final optimized resume is generated

---

## 📊 Reward System

* Score range: **0.0 to 1.0**
* Positive reward → better match
* Negative reward → poor changes

---

## 🧪 Tasks

Located in `/tasks`:

* easy.json
* medium.json
* hard.json

---

## ⚙️ Project Structure

Resume-AI-Openenv/
│
├── env/
├── tasks/
├── app.py
├── inference.py
├── openenv.yaml
├── requirements.txt
├── Dockerfile
└── README.md

---

## ▶️ Run Locally

pip install -r requirements.txt
python inference.py

---

## 🌐 Deployment

Hosted on Hugging Face Spaces using Gradio.

---

## 👨‍💻 Author

Suresh 🚀
