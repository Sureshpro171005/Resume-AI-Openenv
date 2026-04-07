---

title: AI Resume Optimizer
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: gradio
app_file: app.py
pinned: false
---

# 🚀 AI Resume Optimizer

An AI-powered system that **automatically improves resumes step-by-step** to better match job descriptions using intelligent optimization and scoring.

---

## 🎯 Problem Statement

Many job seekers struggle to tailor their resumes for specific roles, leading to low ATS (Applicant Tracking System) scores and missed opportunities.

---

## 💡 Solution

This project introduces an **AI Resume Optimization Agent** that:

* Analyzes a resume against job requirements
* Applies intelligent improvements
* Tracks progress using a scoring system
* Visualizes improvement through a graph

---

## 🧠 Key Features

* ✅ Step-by-step resume optimization
* 📊 Score tracking (Initial → Final + improvement %)
* 📈 Graph visualization of improvement
* 💡 Explainable AI (why score improved)
* 🎨 Clean and modern UI (Gradio)
* 🔁 Reproducible environment (OpenEnv-style)

---

## ⚙️ How It Works

1. Load a sample resume and job description
2. Calculate initial similarity score
3. Apply optimization actions:

   * Add relevant skills
   * Improve experience
   * Optimize keywords
4. Recalculate score after each step
5. Display:

   * Final optimized resume
   * Improvement percentage
   * Step-by-step changes
   * Score improvement graph

---

## 📊 Example Output

* Initial Score: `0.36`
* Final Score: `0.40 (+11%)`
* Improvement explained with actions
* Visual graph of score progression

---

## 🏗️ Tech Stack

* Python
* Gradio (UI)
* Matplotlib (Graph visualization)
* Custom similarity scoring (NLP-based logic)

---

## 📁 Project Structure

```plaintext
Resume-AI-Openenv/
│
├── env/
│   ├── __init__.py
│   ├── resume_env.py
│   ├── utils.py
│
├── tasks/
│   ├── easy.json
│   ├── medium.json
│   ├── hard.json
│
├── app.py
├── requirements.txt
├── openenv.yaml
├── Dockerfile
└── README.md
```

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
python app.py
```

---

## 🌐 Live Demo

👉 Deployed on Hugging Face Spaces

---

## 🧪 Use Cases

* Resume optimization tools
* AI career assistants
* ATS score improvement systems
* Educational AI environments

---

## 🏆 Highlights

* Built an **interactive AI system**, not just a static tool
* Demonstrates **step-wise optimization with measurable impact**
* Combines **AI + visualization + UX design**

---

